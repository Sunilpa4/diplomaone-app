// Synthetic, offline-only catalog. Never a production seed or source change.
const keys=['computer','civil','chemical','electrical','mechanical'];
const codes={computer:'DI01000131',civil:'DI03006011',chemical:'DI05005011',electrical:'DI03009011',mechanical:'DI03000161',
 maths:'DI01000021',physics:'DI01000121',shared:'DI02000051',hiddenSemester:'DI06007011',hiddenBranch:'DI04160011',unmapped:'DI09999999'};
const names={computer:['Computer Engineering','કમ્પ્યુટર એન્જિનિયરિંગ'],civil:['Civil Engineering','સિવિલ એન્જિનિયરિંગ'],
 chemical:['Chemical Engineering','કેમિકલ એન્જિનિયરિંગ'],electrical:['Electrical Engineering','ઇલેક્ટ્રિકલ એન્જિનિયરિંગ'],mechanical:['Mechanical Engineering','મિકેનિકલ એન્જિનિયરિંગ']};
function catalog(){
 const labels={computer:['Computer Programming','કમ્પ્યુટર પ્રોગ્રામિંગ'],civil:['Construction Technology','કન્સ્ટ્રક્શન ટેકનોલોજી'],
  chemical:['Mass Transfer - II','માસ ટ્રાન્સફર'],electrical:['Electrical Circuits','ઇલેક્ટ્રિકલ સર્કિટ'],mechanical:['Manufacturing Engineering I','મેન્યુફેક્ચરિંગ એન્જિનિયરિંગ I'],
  maths:['Mathematics - I','ગણિત - I'],physics:['Applied Physics','એપ્લાઇડ ફિઝિક્સ'],shared:['Shared Sustainability','સાંઝો વિષય'],
  hiddenSemester:['Deferred Advanced Course','મુલતવી વિષય'],hiddenBranch:['IT-only Course','આઇટી વિષય'],unmapped:['Unmapped Course','અન્ય આપેલો વિષય']};
 const subjects=Object.fromEntries(Object.entries(codes).map(([key,code])=>[code,{code,alt_code:'ALT_'+code,
  name:{en:labels[key][0],gu:labels[key][1]},status:'available',units:1,languages:['en','gu']} ]));
 const branches=keys.map((key,i)=>({key,code:['07','06','05','09','19'][i],name:{en:names[key][0],gu:names[key][1]},
  icon:['computer','grid','science','bolt','settings'][i],semesters:{'1':[codes.maths,codes.physics],
   [key==='computer'?'2':key==='chemical'?'5':'3']:[codes[key]],'6':[]}}));
 // Shared notes stay visible if at least one current placement exists. Counts
 // must not double-count a code that also appears in another visible semester.
 const computer=branches[0];computer.semesters['1'].push(codes.computer,codes.shared);
 computer.semesters['2'].push(codes.shared);computer.semesters['6']=[codes.hiddenSemester,codes.shared];
 branches.push({key:'it',code:'16',name:{en:'Information Technology',gu:'ઇન્ફોર્મેશન ટેકનોલોજી'},semesters:{'1':[codes.maths,codes.computer], '4':[codes.hiddenBranch], '6':[codes.hiddenSemester]}});
 return {branches,subjects};
}
const session='summer-2026';
function tree(){return {truncated:false,tree:[...new Set([...Object.values(codes),'4350501'])].map(code=>({type:'blob',mode:'100644',path:`papers/${code}/${session}.${[codes.maths,codes.physics].includes(code)?'html':'json'}`}))};}
function subject(code,c){return {code,name:c.subjects[code].name,languages:['en','gu'],units:[{no:1,title:{en:'First unit',gu:'પહેલો એકમ'}},{no:6,title:{en:'Sixth unit',gu:'છઠ્ઠો એકમ'}}],available_units:[1,6]};}
function unit(code,num){return {code,unit:Number(num),title:{en:'Offline unit '+num,gu:'મૂળ એકમ '+num},languages:['en','gu'],
 notes:[{title:{en:'Preserved notes',gu:'યથાવત્ નોટ્સ'},body:'<p>OFFLINE NOTE CONTENT</p>'}]};}
const freeReader='<main><section><h2>Question 1</h2><details class="card"><summary><strong class="en">Free question</strong><strong class="gu">મફત પ્રશ્ન</strong></summary><div class="answer"><p class="en">FREE ANSWER FIXTURE</p><p class="gu">મફત જવાબ</p></div></details></section></main>';
const ownedReader='<main><section><h2>Question 1</h2><details class="card"><summary>Owned historical question</summary><div class="answer">OWNED PRIVATE FIXTURE</div></details></section></main>';
module.exports={keys,codes,names,catalog,tree,subject,unit,session,freeReader,ownedReader};
