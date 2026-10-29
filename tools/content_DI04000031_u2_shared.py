"""Pure MongoDB Unit 2 fixtures: no connections or database dependencies.

SEED is included verbatim in every relevant displayed script, not hidden setup.
"""
STUDENTS = [
    {'_id': 1, 'name': 'Asha', 'age': 19, 'city': 'Surat', 'marks': 82, 'active': True,
     'skills': ['MongoDB', 'Python'], 'address': {'state': 'Gujarat', 'pin': '395001'}},
    {'_id': 2, 'name': 'Ravi', 'age': 20, 'city': 'Bharuch', 'marks': 70, 'active': True,
     'skills': ['Java'], 'address': {'state': 'Gujarat', 'pin': '392001'}},
    {'_id': 3, 'name': 'Neha', 'age': 18, 'city': 'Surat', 'marks': 92, 'active': True,
     'skills': ['MongoDB', 'Java'], 'address': {'state': 'Gujarat', 'pin': '395007'}},
    {'_id': 4, 'name': 'Imran', 'age': 21, 'city': 'Vadodara', 'marks': 65, 'active': False,
     'skills': ['Python'], 'address': {'state': 'Gujarat', 'pin': '390001'}},
    {'_id': 5, 'name': 'Meera', 'age': 20, 'city': 'Surat', 'marks': 82, 'active': True,
     'skills': ['AI', 'Python'], 'address': {'state': 'Gujarat', 'pin': '395009'}},
    {'_id': 6, 'name': 'Dev', 'age': 19, 'city': 'Ahmedabad', 'marks': 50, 'active': False,
     'skills': [], 'address': {'state': 'Gujarat', 'pin': '380001'}},
]

SEED = '''db.students.insertMany([
  {_id: 1, name: "Asha", age: 19, city: "Surat",
   marks: 82, active: true, skills: ["MongoDB", "Python"],
   address: {state: "Gujarat", pin: "395001"}},
  {_id: 2, name: "Ravi", age: 20, city: "Bharuch",
   marks: 70, active: true, skills: ["Java"],
   address: {state: "Gujarat", pin: "392001"}},
  {_id: 3, name: "Neha", age: 18, city: "Surat",
   marks: 92, active: true, skills: ["MongoDB", "Java"],
   address: {state: "Gujarat", pin: "395007"}},
  {_id: 4, name: "Imran", age: 21, city: "Vadodara",
   marks: 65, active: false, skills: ["Python"],
   address: {state: "Gujarat", pin: "390001"}},
  {_id: 5, name: "Meera", age: 20, city: "Surat",
   marks: 82, active: true, skills: ["AI", "Python"],
   address: {state: "Gujarat", pin: "395009"}},
  {_id: 6, name: "Dev", age: 19, city: "Ahmedabad",
   marks: 50, active: false, skills: [],
   address: {state: "Gujarat", pin: "380001"}}
]);
'''
IDS = '''const ids = q => db.students.find(q, {_id: 1})
  .sort({_id: 1}).toArray().map(x => x._id);
'''
