"""Complete student-facing PHP applications for Practicals 20-23. No execution on import."""

BLOG = r'''
<?php
require __DIR__ . "/web.php";
function findPost(mysqli $db, int $id): ?array {
    $s = $db->prepare("SELECT * FROM posts WHERE id=?");
    $s->bind_param("i", $id);
    $s->execute();
    $row = $s->get_result()->fetch_assoc();
    $s->close();
    return $row;
}
$error = "";
$edit = ["id" => 0, "title" => "", "body" => ""];
if ($_SERVER["REQUEST_METHOD"] === "POST") {
    check_csrf();
    $action = text($_POST, "action");
    if ($action === "delete") {
        $id = positiveId($_POST["id"] ?? null);
        $s = $db->prepare("DELETE FROM posts WHERE id=?");
        $s->bind_param("i", $id);
        $s->execute();
        if ($s->affected_rows !== 1) {
            fail("Post not found.", 404);
        }
        redirect("Post deleted.");
    }
    if ($action !== "save") {
        fail("Unknown action.");
    }
    $id = recordId($_POST["id"] ?? 0);
    $title = text($_POST, "title");
    $body = text($_POST, "body");
    $edit = ["id" => $id, "title" => $title, "body" => $body];
    if ($id > 0 && !findPost($db, $id)) {
        fail("Post not found.", 404);
    }
    if ($title === "" || strlen($title) > 100
        || $body === "" || strlen($body) > 5000) {
        http_response_code(422);
        $error = "Title (1-100) and body (1-5000) are required.";
    } else {
        if ($id === 0) {
            $s = $db->prepare("INSERT INTO posts(title,body) VALUES (?,?)");
            $s->bind_param("ss", $title, $body);
        } else {
            $s = $db->prepare("UPDATE posts SET title=?,body=? WHERE id=?");
            $s->bind_param("ssi", $title, $body, $id);
        }
        $s->execute();
        redirect($id === 0 ? "Post created." : "Post updated.");
    }
} elseif (isset($_GET["edit"])) {
    $id = positiveId($_GET["edit"]);
    $edit = findPost($db, $id);
    if (!$edit) {
        fail("Post not found.", 404);
    }
}
$q = text($_GET, "q");
$like = "%$q%";
$s = $db->prepare("SELECT * FROM posts WHERE title LIKE ? ORDER BY id DESC");
$s->bind_param("s", $like);
$s->execute();
$rows = $s->get_result()->fetch_all(MYSQLI_ASSOC);
$s->close();
page("BusBook Blog");
?>
<p><?= e($error) ?></p>
<form method="get">
  <input name="q" value="<?= e($q) ?>" placeholder="Search title">
  <button>Search</button>
</form>
<form method="post">
  <?= csrf_field() ?>
  <input type="hidden" name="action" value="save">
  <input type="hidden" name="id" value="<?= (int)$edit['id'] ?>">
  <input name="title" maxlength="100" required value="<?= e($edit['title']) ?>">
  <textarea name="body" required><?= e($edit['body']) ?></textarea>
  <button>Save post</button>
</form>
<p>Posts: <?= count($rows) ?></p>
<?php foreach ($rows as $post): ?>
<article data-id="<?= (int)$post['id'] ?>">
  <h2><?= e($post['title']) ?></h2>
  <p><?= nl2br(e($post['body'])) ?></p>
  <a href="?edit=<?= (int)$post['id'] ?>">Edit</a>
  <form method="post">
    <?= csrf_field() ?>
    <input type="hidden" name="action" value="delete">
    <input type="hidden" name="id" value="<?= (int)$post['id'] ?>">
    <button>Delete post</button>
  </form>
</article>
<?php endforeach; ?>
'''

CONTACT_INDEX = r'''
<?php
require __DIR__ . "/web.php";
require __DIR__ . "/app/Contact.php";
require __DIR__ . "/app/ContactController.php";
$model = new Contact($db);
$controller = new ContactController($model);
$controller->handle();
'''

CONTACT_MODEL = r'''
<?php
class Contact {
    private mysqli $db;
    public function __construct(mysqli $db) {
        $this->db = $db;
    }
    public function search(string $q): array {
        $sql = "SELECT id,name,email FROM contacts "
             . "WHERE name LIKE ? OR email LIKE ? ORDER BY id";
        $s = $this->db->prepare($sql);
        $like = "%$q%";
        $s->bind_param("ss", $like, $like);
        $s->execute();
        $rows = $s->get_result()->fetch_all(MYSQLI_ASSOC);
        $s->close();
        return $rows;
    }
    public function find(int $id): ?array {
        $s = $this->db->prepare("SELECT * FROM contacts WHERE id=?");
        $s->bind_param("i", $id);
        $s->execute();
        $row = $s->get_result()->fetch_assoc();
        $s->close();
        return $row;
    }
    public function save(int $id, string $name, string $email): void {
        if ($id === 0) {
            $s = $this->db->prepare(
                "INSERT INTO contacts(name,email) VALUES (?,?)"
            );
            $s->bind_param("ss", $name, $email);
        } else {
            $s = $this->db->prepare(
                "UPDATE contacts SET name=?,email=? WHERE id=?"
            );
            $s->bind_param("ssi", $name, $email, $id);
        }
        $s->execute();
        $s->close();
    }
    public function delete(int $id): bool {
        $s = $this->db->prepare("DELETE FROM contacts WHERE id=?");
        $s->bind_param("i", $id);
        $s->execute();
        $deleted = $s->affected_rows === 1;
        $s->close();
        return $deleted;
    }
}
'''

CONTACT_CONTROLLER = r'''
<?php
class ContactController {
    private Contact $model;
    public function __construct(Contact $model) {
        $this->model = $model;
    }
    public function handle(): void {
        $error = "";
        $edit = ["id" => 0, "name" => "", "email" => ""];
        if ($_SERVER["REQUEST_METHOD"] === "POST") {
            check_csrf();
            $action = text($_POST, "action");
            if ($action === "delete") {
                $id = positiveId($_POST["id"] ?? null);
                if (!$this->model->delete($id)) {
                    fail("Contact not found.", 404);
                }
                redirect("Contact deleted.");
            }
            if ($action !== "save") {
                fail("Unknown action.");
            }
            $id = recordId($_POST["id"] ?? 0);
            $name = text($_POST, "name");
            $email = text($_POST, "email");
            $edit = ["id" => $id, "name" => $name, "email" => $email];
            if ($id > 0 && !$this->model->find($id)) {
                fail("Contact not found.", 404);
            }
            if (strlen($name) < 2 || strlen($name) > 80
                || strlen($email) > 120
                || !filter_var($email, FILTER_VALIDATE_EMAIL)) {
                http_response_code(422);
                $error = "Name (2-80) and a valid email are required.";
            } else {
                $this->model->save($id, $name, $email);
                redirect($id === 0 ? "Contact added." : "Contact updated.");
            }
        } elseif (isset($_GET["edit"])) {
            $id = positiveId($_GET["edit"]);
            $edit = $this->model->find($id);
            if (!$edit) {
                fail("Contact not found.", 404);
            }
        }
        $q = text($_GET, "q");
        $rows = $this->model->search($q);
        require __DIR__ . "/../views/contacts.php";
    }
}
'''

CONTACT_VIEW = r'''
<?php page("MVC Contacts"); ?>
<p><?= e($error) ?></p>
<form method="get">
  <input name="q" placeholder="Search name/email" value="<?= e($q) ?>">
  <button>Search</button>
</form>
<form method="post">
  <?= csrf_field() ?>
  <input type="hidden" name="action" value="save">
  <input type="hidden" name="id" value="<?= (int)$edit['id'] ?>">
  <input name="name" maxlength="80" required value="<?= e($edit['name']) ?>">
  <input name="email" type="email" required value="<?= e($edit['email']) ?>">
  <button>Save contact</button>
</form>
<p>Contacts: <?= count($rows) ?></p>
<?php foreach ($rows as $contact): ?>
<article data-id="<?= (int)$contact['id'] ?>">
  <b><?= e($contact['name']) ?></b>
  <span><?= e($contact['email']) ?></span>
  <a href="?edit=<?= (int)$contact['id'] ?>">Edit</a>
  <form method="post">
    <?= csrf_field() ?>
    <input type="hidden" name="action" value="delete">
    <input type="hidden" name="id" value="<?= (int)$contact['id'] ?>">
    <button>Delete contact</button>
  </form>
</article>
<?php endforeach; ?>
'''

TODO = r'''
<?php
require __DIR__ . "/web.php";
$edit = ["id" => 0, "title" => ""];
$error = "";
if ($_SERVER["REQUEST_METHOD"] === "POST") {
    check_csrf();
    $action = text($_POST, "action");
    if ($action === "toggle" || $action === "delete") {
        $id = positiveId($_POST["id"] ?? null);
        $sql = $action === "toggle"
             ? "UPDATE todos SET done=1-done WHERE id=?"
             : "DELETE FROM todos WHERE id=?";
        $s = $db->prepare($sql);
        $s->bind_param("i", $id);
        $s->execute();
        if ($s->affected_rows !== 1) {
            fail("Task not found.", 404);
        }
        redirect($action === "toggle" ? "Status changed." : "Task deleted.");
    }
    if ($action !== "save") {
        fail("Unknown action.");
    }
    $id = recordId($_POST["id"] ?? 0);
    $title = text($_POST, "title");
    $edit = ["id" => $id, "title" => $title];
    if ($id > 0) {
        $s = $db->prepare("SELECT id FROM todos WHERE id=?");
        $s->bind_param("i", $id);
        $s->execute();
        if (!$s->get_result()->fetch_assoc()) {
            fail("Task not found.", 404);
        }
    }
    if ($title === "" || strlen($title) > 150) {
        http_response_code(422);
        $error = "Title must contain 1-150 characters.";
    } else {
        if ($id === 0) {
            $s = $db->prepare("INSERT INTO todos(title) VALUES (?)");
            $s->bind_param("s", $title);
        } else {
            $s = $db->prepare("UPDATE todos SET title=? WHERE id=?");
            $s->bind_param("si", $title, $id);
        }
        $s->execute();
        redirect($id === 0 ? "Task added." : "Task updated.");
    }
} elseif (isset($_GET["edit"])) {
    $id = positiveId($_GET["edit"]);
    $s = $db->prepare("SELECT id,title FROM todos WHERE id=?");
    $s->bind_param("i", $id);
    $s->execute();
    $edit = $s->get_result()->fetch_assoc();
    if (!$edit) {
        fail("Task not found.", 404);
    }
}
$filter = text($_GET, "filter") ?: "all";
// Only trusted SQL fragments; never concatenate a submitted clause.
$conditions = [
    "all" => "", "pending" => " WHERE done=0",
    "done" => " WHERE done=1"
];
if (!array_key_exists($filter, $conditions)) {
    fail("Unknown filter.");
}
$sql = "SELECT * FROM todos" . $conditions[$filter] . " ORDER BY id";
$rows = $db->query($sql)->fetch_all(MYSQLI_ASSOC);
page("Study To-Do List");
?>
<p><?= e($error) ?></p>
<a href="?filter=all">All</a>
<a href="?filter=pending">Pending</a>
<a href="?filter=done">Done</a>
<form method="post">
  <?= csrf_field() ?>
  <input type="hidden" name="action" value="save">
  <input type="hidden" name="id" value="<?= (int)$edit['id'] ?>">
  <input name="title" maxlength="150" required value="<?= e($edit['title']) ?>">
  <button>Save task</button>
</form>
<p>Tasks: <?= count($rows) ?></p>
<?php foreach ($rows as $task): ?>
<article data-id="<?= (int)$task['id'] ?>">
  <span><?= e($task['title']) ?></span>
  <b><?= $task['done'] ? "Done" : "Pending" ?></b>
  <a href="?edit=<?= (int)$task['id'] ?>">Edit</a>
  <form method="post">
    <?= csrf_field() ?>
    <input type="hidden" name="id" value="<?= (int)$task['id'] ?>">
    <button name="action" value="toggle">Toggle done</button>
    <button name="action" value="delete">Delete task</button>
  </form>
</article>
<?php endforeach; ?>
'''

INVENTORY_AUTH = r'''
<?php
require_once __DIR__ . "/web.php";
$adminHash = getenv("ADMIN_HASH") ?: "";
if ($adminHash === "") {
    fail("Configure ADMIN_HASH before using inventory.", 503);
}
$error = "";
if (!isset($_SESSION["admin"])) {
    if ($_SERVER["REQUEST_METHOD"] === "POST") {
        check_csrf();
        if (text($_POST, "action") !== "login") {
            fail("Sign in first.", 401);
        }
        $user = text($_POST, "username");
        // Do not trim a password: spaces can be intentional.
        $pass = $_POST["password"] ?? null;
        if ($user === "admin" && is_string($pass)
            && password_verify($pass, $adminHash)) {
            session_regenerate_id(true);
            $_SESSION["admin"] = true;
            $_SESSION["csrf"] = bin2hex(random_bytes(16));
            redirect("Signed in.");
        }
        http_response_code(401);
        $error = "Invalid username or password.";
    }
    page("Inventory Login");
    echo '<p>', e($error), '</p>';
    echo '<form method="post">', csrf_field();
    echo '<input type="hidden" name="action" value="login">';
    echo '<input name="username" required placeholder="Username">';
    echo '<input name="password" type="password" required>';
    echo '<button>Log in</button></form>';
    exit;
}
if ($_SERVER["REQUEST_METHOD"] === "POST"
    && text($_POST, "action") === "logout") {
    check_csrf();
    $_SESSION = [];
    $p = session_get_cookie_params();
    setcookie(session_name(), "", [
        "expires" => time() - 3600, "path" => $p["path"],
        "domain" => $p["domain"], "secure" => $p["secure"],
        "httponly" => $p["httponly"],
        "samesite" => $p["samesite"] ?? "Lax"
    ]);
    session_destroy();
    header("Location: index.php", true, 303);
    exit;
}
'''

INVENTORY = r'''
<?php
require __DIR__ . "/auth.php";
function product(mysqli $db, int $id): ?array {
    $s = $db->prepare("SELECT * FROM products WHERE id=?");
    $s->bind_param("i", $id);
    $s->execute();
    return $s->get_result()->fetch_assoc();
}
$error = "";
$edit = ["id" => 0, "sku" => "", "name" => "", "qty" => "0", "price" => "0.00"];
if ($_SERVER["REQUEST_METHOD"] === "POST") {
    check_csrf();
    $action = text($_POST, "action");
    if (in_array($action, ["delete", "sell", "restock"], true)) {
        $id = positiveId($_POST["id"] ?? null);
        if (!product($db, $id)) {
            fail("Product not found.", 404);
        }
        if ($action === "delete") {
            $s = $db->prepare("DELETE FROM products WHERE id=?");
            $s->bind_param("i", $id);
            $s->execute();
            redirect("Product deleted.");
        }
        $amount = filter_var($_POST["amount"] ?? null, FILTER_VALIDATE_INT, [
            "options" => ["min_range" => 1, "max_range" => 1000000]
        ]);
        if ($amount === false) {
            fail("Amount must be a positive integer.", 422);
        }
        $sql = $action === "sell"
             ? "UPDATE products SET qty=qty-? WHERE id=? AND qty>=?"
             : "UPDATE products SET qty=qty+? WHERE id=? AND qty<=1000000-?";
        $s = $db->prepare($sql);
        $s->bind_param("iii", $amount, $id, $amount);
        $s->execute();
        if ($s->affected_rows !== 1) {
            fail("Stock change rejected; quantity unchanged.", 409);
        }
        redirect("Stock changed.");
    }
    if ($action !== "save") {
        fail("Unknown action.");
    }
    $id = recordId($_POST["id"] ?? 0);
    $sku = text($_POST, "sku");
    $name = text($_POST, "name");
    $qtyText = text($_POST, "qty");
    $price = text($_POST, "price");
    $qty = filter_var($qtyText, FILTER_VALIDATE_INT, [
        "options" => ["min_range" => 0, "max_range" => 1000000]
    ]);
    $edit = ["id" => $id, "sku" => $sku, "name" => $name,
             "qty" => $qtyText, "price" => $price];
    if ($id > 0 && !product($db, $id)) {
        fail("Product not found.", 404);
    }
    if (!preg_match('/^[A-Za-z0-9_-]{1,30}$/', $sku)
        || $name === "" || strlen($name) > 80 || $qty === false
        || !preg_match('/^\d{1,7}(?:\.\d{1,2})?$/', $price)) {
        $error = "Use a valid SKU/name, non-negative integer qty and price (max 2 decimals).";
    } else {
        try {
            if ($id === 0) {
                $s = $db->prepare(
                    "INSERT INTO products(sku,name,qty,price) VALUES (?,?,?,?)"
                );
                $s->bind_param("ssis", $sku, $name, $qty, $price);
            } else {
                $s = $db->prepare(
                    "UPDATE products SET sku=?,name=?,qty=?,price=? WHERE id=?"
                );
                $s->bind_param("ssisi", $sku, $name, $qty, $price, $id);
            }
            $s->execute();
            redirect($id === 0 ? "Product added." : "Product updated.");
        } catch (mysqli_sql_exception $e) {
            if ($e->getCode() !== 1062) {
                throw $e;
            }
            $error = "SKU already exists.";
        }
    }
    http_response_code(422);
} elseif (isset($_GET["edit"])) {
    $edit = product($db, positiveId($_GET["edit"]));
    if (!$edit) {
        fail("Product not found.", 404);
    }
}
$rows = $db->query("SELECT * FROM products ORDER BY id")->fetch_all(MYSQLI_ASSOC);
page("Inventory Manager");
?>
<form method="post">
  <?= csrf_field() ?>
  <button name="action" value="logout">Log out</button>
</form>
<p><?= e($error) ?></p>
<form method="post">
  <?= csrf_field() ?>
  <input type="hidden" name="action" value="save">
  <input type="hidden" name="id" value="<?= (int)$edit['id'] ?>">
  SKU: <input name="sku" required value="<?= e($edit['sku']) ?>"><br>
  Name: <input name="name" required value="<?= e($edit['name']) ?>"><br>
  Quantity: <input name="qty" type="number" min="0" required value="<?= e((string)$edit['qty']) ?>"><br>
  Price: <input name="price" type="number" step="0.01" min="0" required value="<?= e((string)$edit['price']) ?>"><br>
  <button>Save product</button>
</form>
<p>Products: <?= count($rows) ?></p>
<?php foreach ($rows as $p): ?>
<article data-id="<?= (int)$p['id'] ?>">
  <b><?= e($p['sku']) ?>: <?= e($p['name']) ?></b>
  <p>Qty: <?= (int)$p['qty'] ?> | Price: Rs <?= e($p['price']) ?></p>
  <?php if ($p['qty'] <= 3): ?><strong>Low stock</strong><?php endif; ?>
  <a href="?edit=<?= (int)$p['id'] ?>">Edit</a>
  <form method="post">
    <?= csrf_field() ?>
    <input type="hidden" name="id" value="<?= (int)$p['id'] ?>">
    <input name="amount" type="number" min="1" value="1">
    <button name="action" value="sell">Sell</button>
    <button name="action" value="restock">Restock</button>
    <button name="action" value="delete">Delete</button>
  </form>
</article>
<?php endforeach; ?>
'''
