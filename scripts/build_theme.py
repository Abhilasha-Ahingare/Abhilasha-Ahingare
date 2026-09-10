"""Generate the README and editable SVG assets. Python 3.10+; no packages."""
from pathlib import Path
import sys
from theme import *

ROOT = Path(__file__).resolve().parents[1]
ASSETS = ROOT / 'assets'
USER = 'Abhilasha-Ahingare'
EMAIL = 'abhilashaahingare.02@gmail.com'
TECH = {
    'Languages': [('html5','HTML5'),('css3','CSS3'),('javascript','JavaScript'),('typescript','TypeScript')],
    'Frontend & styling': [('react','React'),('remix','Remix'),('react-router','React Router'),('redux','Redux'),('tailwindcss','Tailwind CSS'),('bootstrap','Bootstrap'),('mui','MUI'),('sass','Sass'),('vite','Vite')],
    'Backend & data': [('nodejs','Node.js'),('ejs','EJS'),('mongodb','MongoDB'),('mysql','MySQL')],
    'Tools & design': [('git','Git'),('github','GitHub'),('npm','npm'),('nodemon','Nodemon'),('canva','Canva')],
}

def write(name, value):
    path = ASSETS / name
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(value, encoding='utf-8')

def badge(label, accent=False):
    w = max(88, round(len(label)*7.4+43))
    body = rect(1,1,w-2,34,'#221b32' if accent else PANEL,'#493561' if accent else BORDER,7)
    body += f'<circle cx="15" cy="18" r="3" fill="{ACCENT}"/>'
    body += text(28,23,label,13,ACCENT if accent else TEXT,600)
    return svg(w,36,body,label,background=False)

def hero(mobile=False):
    w,h = (600,370) if mobile else (1000,330)
    body = f'''<defs>
      <radialGradient id="light" cx="96%" cy="0%" r="98%"><stop stop-color="#8657cf" stop-opacity=".76"/><stop offset=".46" stop-color="#302448" stop-opacity=".48"/><stop offset="1" stop-color="#11141b" stop-opacity="0"/></radialGradient>
      <radialGradient id="spark"><stop stop-color="#dfcdff"/><stop offset=".22" stop-color="#bc8aff"/><stop offset="1" stop-color="#a06cff" stop-opacity="0"/></radialGradient>
    </defs>'''
    body += rect(1,1,w-2,h-2,'url(#light)','none',14)
    if mobile:
        body += '<ellipse cx="496" cy="87" rx="103" ry="24" transform="rotate(-31 496 87)" fill="none" stroke="#83649e" stroke-opacity=".45"/>'
        body += '<circle cx="530" cy="91" r="24" fill="url(#spark)"/><circle cx="530" cy="91" r="5" fill="#cda8ff"/>'
        body += text(300,58,'FRONTEND DEVELOPER',13,MUTED,500,'middle',letter_spacing=4)
        body += text(300,145,'Abhilasha',66,TEXT,700,'middle')
        body += text(300,211,'Ahingare',66,TEXT,700,'middle')
        body += text(300,266,'Thoughtful interfaces.',22,MUTED,400,'middle')
        body += text(300,297,'Practical web experiences.',22,MUTED,400,'middle')
        body += text(300,342,'REACT  ·  JAVASCRIPT  ·  TYPESCRIPT',12,TEXT,400,'middle',letter_spacing=2)
    else:
        body += '<ellipse cx="840" cy="130" rx="130" ry="25" transform="rotate(-30 840 130)" fill="none" stroke="#9473b7" stroke-opacity=".45"/>'
        body += '<circle cx="885" cy="134" r="25" fill="url(#spark)"/><circle cx="885" cy="134" r="6" fill="#cda8ff"/>'
        body += text(500,82,'FRONTEND DEVELOPER',13,MUTED,500,'middle',letter_spacing=5)
        body += text(500,162,'Abhilasha Ahingare',64,TEXT,700,'middle')
        body += text(500,210,'Thoughtful interfaces. Practical web experiences.',22,MUTED,400,'middle')
        body += text(500,255,'REACT  ·  JAVASCRIPT  ·  TYPESCRIPT',13,TEXT,400,'middle',letter_spacing=2.5)
        for i,label in enumerate(['CODE','SOLVE','BUILD','REPEAT']):
            body += text(38,127+i*17,label,9,MUTED,400,letter_spacing=3)
        body += line(38,195,66,195,'#5b536b',2)
        for i,label in enumerate(['SIMPLE','IDEAS','BETTER','SOFTWARE']):
            body += text(962,228+i*15,label,8,MUTED,400,'end',letter_spacing=2)
    return svg(w,h,body,'Abhilasha Ahingare — Frontend Developer','Thoughtful interfaces. Practical web experiences. React, JavaScript and TypeScript.')

def core_stack(mobile=False):
    w,h=(600,102) if mobile else (1000,64)
    labels=['React','JavaScript','TypeScript','Node.js','MongoDB','MySQL']
    body=''
    for i,label in enumerate(labels):
        cols=3 if mobile else 6
        x=30+(i%cols)*(190 if mobile else 162)
        y=31+(i//cols)*43 if mobile else 36
        body += f'<circle cx="{x}" cy="{y-5}" r="4" fill="{ACCENT}"/>'+text(x+15,y,label,15,TEXT)
        if i%cols<cols-1:body+=line(x+(165 if mobile else 142),y-15,x+(165 if mobile else 142),y+4)
    return svg(w,h,body,'Core technologies',', '.join(labels))

def section(title, caption='', mobile=False):
    w=600 if mobile else 1000
    body=text(4,44,title,34 if mobile else 36,TEXT,700)
    start=min(w-55,len(title)*21+36)
    body+=line(start,35,w-8,35)
    return svg(w,68,body,title,caption,False)

def project_art(kind):
    body='''<defs><linearGradient id="projectLight" x1="0" y1="0" x2="1" y2="1"><stop stop-color="#312340"/><stop offset="1" stop-color="#11141b"/></linearGradient><linearGradient id="glass"><stop stop-color="#7652b6" stop-opacity=".9"/><stop offset="1" stop-color="#352447" stop-opacity=".4"/></linearGradient></defs>'''
    body+=rect(0,0,430,213,'url(#projectLight)',BORDER,9)
    if kind=='admin':
        body+=rect(43,27,336,163,'#191721','#493763',9)
        body+=rect(43,27,64,163,'#211c2e','none',9)
        body+=text(59,53,'A',16,ACCENT,700)
        for yy in [72,96,120,144]:body+=rect(58,yy,33,5,'#514265','none',2)
        for i in range(3):
            xx=125+i*78
            body+=rect(xx,51,64,37,'#302440','#594075',5)
            body+=line(xx+11,63,xx+30,63,ACCENT,3)+line(xx+11,74,xx+44,74,'#68517f',3)
        body+='<path d="M133 157L163 146 195 151 225 118 253 128 283 112 330 107" fill="none" stroke="#b28aff" stroke-width="3"/>'
        body+=line(126,171,356,171,'#403448')
        body+='<circle cx="283" cy="112" r="5" fill="#dec8ff"/>'
    else:
        body+=rect(75,59,220,125,'#221b31','#423352',12)
        body+=rect(119,27,237,135,'url(#glass)','#7356a0',12)
        body+='<path d="M297 158L327 182 323 156Z" fill="#443056" stroke="#7356a0"/>'
        for i in range(3):
            yy=57+i*32
            body+=f'<circle cx="150" cy="{yy}" r="6" fill="#e2cfff"/>'
            body+=line(170,yy,287-(i%2)*30,yy,'#bba3d6',4)
        body+=rect(48,140,101,40,'#322544','#69488d',10)
        for xx in [77,98,119]:body+=f'<circle cx="{xx}" cy="160" r="4" fill="#c6a5f3"/>'
    return body.replace('projectLight',kind+'Light').replace('glass',kind+'Glass')

def projects(mobile=False):
    w,h=(600,810) if mobile else (1000,401)
    items=[('MERN Admin Panel','Authentication & service management','MERN stack','admin'),('Chat App','A web chat project','JavaScript','chat')]
    body=''
    for i,(name,desc,stack,kind) in enumerate(items):
        x,y=(1,i*405+1) if mobile else (i*511+1,1)
        cw=598 if mobile else 487
        card=rect(0,0,cw-1,391,PANEL,BORDER,10)
        scale=(cw-48)/430
        card+=f'<g transform="translate(24 22) scale({scale:.4f} {(.98 if mobile else .98):.4f})">{project_art(kind)}</g>'
        card+=text(24,271,name,30,TEXT,700)+text(24,305,desc,18,MUTED)
        card+=rect(24,330,151,30,'#261d35','#443255',15)+text(39,350,'Source available',13,ACCENT,500)
        card+=text(cw-25,350,stack,13,MUTED,400,'end')
        body+=f'<g transform="translate({x} {y})">{card}</g>'
    return svg(w,h,body,'Selected projects: MERN Admin Panel and Chat App','Project illustrations are decorative, not application screenshots. Repository links follow below.',False)

def about(mobile=False):
    w,h=(600,270) if mobile else (1000,232)
    body=text(30,49,'What I build',29,TEXT,700)
    if mobile:
        lines=['React interfaces. Responsive layouts.','Practical web projects with the MERN stack.']
        for i,value in enumerate(lines):body+=text(30,91+i*31,value,20,MUTED)
        body+=line(30,145,570,145)
        body+=text(30,178,'NOW',12,ACCENT,700,letter_spacing=2)+text(103,178,'Frontend projects',17,TEXT)
        body+=text(30,213,'LEARNING',12,ACCENT,700,letter_spacing=1)+text(135,213,'Express.js',17,TEXT)
        body+=text(30,246,'ASK ME',12,ACCENT,700,letter_spacing=1)+text(135,246,'MERN development',17,TEXT)
    else:
        body+=text(30,92,'React interfaces. Responsive layouts. Practical web projects.',23,MUTED)
        body+=line(30,118,970,118)
        for x,label,value in [(30,'NOW','Frontend projects'),(360,'LEARNING','Express.js'),(690,'ASK ME','MERN development')]:
            body+=text(x,154,label,12,ACCENT,700,letter_spacing=2)+text(x,190,value,20,TEXT,500)
    return svg(w,h,body,'About Abhilasha','Frontend developer from India. Working on frontend projects, learning Express.js, and happy to discuss MERN development.')

def footer(mobile=False):
    w,h=(600,149) if mobile else (1000,137)
    body=line(w/2-25,21,w/2+25,21,'#5c426e',2)
    body+=text(w/2,66,"Let's build something useful.",26,TEXT,600,'middle')
    body+=text(w/2,102,'abhilashaahingare.02@gmail.com',17,ACCENT,500,'middle')
    return svg(w,h,body,'Contact Abhilasha',EMAIL,False)

def picture(name,alt,width='100%'):
    return f'<picture>\n  <source media="(max-width: 600px)" srcset="./assets/{name}-mobile.svg">\n  <img src="./assets/{name}.svg" width="{width}" alt="{escape(alt,quote=True)}">\n</picture>'

def make_readme():
    parts=[f'<!-- Violet Signal / Design 29. Profile: {USER}. Edit scripts/build_theme.py to regenerate this file. -->',
           picture('hero','Abhilasha Ahingare — Frontend Developer. Thoughtful interfaces. Practical web experiences.'),
           picture('core-stack','React, JavaScript, TypeScript, Node.js, MongoDB and MySQL'),
           '<p align="center">\n  <a href="mailto:'+EMAIL+'"><img src="./assets/badges/email.svg" height="36" alt="Email Abhilasha"></a>\n  <a href="https://github.com/'+USER+'?tab=repositories"><img src="./assets/badges/repositories.svg" height="36" alt="Browse all repositories"></a>\n</p>',
           picture('section-projects','Selected projects'),picture('projects','MERN Admin Panel — authentication and service management. Chat App — a web chat project.'),
           '<p align="center">\n  <a href="https://github.com/'+USER+'/adimn-pannel"><img src="./assets/badges/admin-source.svg" height="36" alt="MERN Admin Panel repository"></a>\n  <a href="https://github.com/'+USER+'/chat-app"><img src="./assets/badges/chat-source.svg" height="36" alt="Chat App repository"></a>\n</p>',
           '<details>\n<summary>More projects &amp; learning repositories</summary>\n\n'+ '\n'.join(f'- [{label}](https://github.com/{USER}/{slug})' for slug,label in [('Event-Management-Ticketing-System','Event Management & Ticketing System'),('REACT-PROJECT','React Projects'),('MERN-STACK-PROJECTS','MERN Stack Projects'),('HTML_CSS_JAVASCRIPT_PROJECTS','HTML, CSS & JavaScript Projects'),('HTML-CSS-PROJECTS','HTML & CSS Projects'),('JAVASCRIPT-MINI-FUNCTIONALITY-PROJECT-S','JavaScript Mini Projects')])+'\n\n</details>',
           picture('about','About me: frontend developer from India; building frontend projects; learning Express.js; ask me about MERN development.'),
           picture('section-stack','Tech stack')]
    for group,items in TECH.items():
        parts.append(f'**{group}**\n\n<p>\n'+'\n'.join(f'  <img src="./assets/badges/{slug}.svg" height="36" alt="{label}">' for slug,label in items)+'\n</p>')
    parts.append('**Currently learning**\n\n<img src="./assets/badges/express-learning.svg" height="36" alt="Learning Express.js">')
    parts.append(picture('section-activity','GitHub activity'))
    for name,alt in [('overview','Public GitHub overview'),('streak','Current and longest contribution streaks'),('languages','Languages by code bytes across public repositories'),('calendar','Violet contribution calendar — daily counts available in the data folder'),('top-repos','Top contributed repositories — GitHub-attributed commits in owned public repositories')]:
        parts.append(picture('metrics/'+name,alt))
    parts.append('<details>\n<summary>Activity details &amp; repository links</summary>\n\n- [Daily contribution table and repository ranking](./data/ACTIVITY.md)\n- [Complete metrics snapshot](./data/metrics.json)\n\nCards refresh through the included GitHub Actions workflow. The contribution calendar covers the latest 365 days; streaks use the available history from the account-creation year. Language percentages describe repository code, not proficiency. The repository ranking includes owned public repositories and uses GitHub-attributed commit counts.\n\n</details>')
    parts.append(picture('metrics/quote','Daily dev quote — an original Violet Signal development note'))
    parts.append('<a href="mailto:'+EMAIL+'">\n'+picture('footer','Email Abhilasha: '+EMAIL)+'\n</a>')
    parts.append('<p align="center">\n  <img src="https://komarev.com/ghpvc/?username='+USER+'&amp;label=Profile+views&amp;color=7650ab&amp;style=flat" alt="Profile image request counter">\n</p>')
    return '\n\n'.join(parts)+'\n'

def main():
    for mobile in [False,True]:
        suffix='-mobile' if mobile else ''
        for name,fn in [('hero',hero),('core-stack',core_stack),('projects',projects),('about',about),('footer',footer)]:write(name+suffix+'.svg',fn(mobile))
        for slug,label in [('projects','Projects'),('stack','Tech stack'),('activity','GitHub activity')]:write('section-'+slug+suffix+'.svg',section(label,mobile=mobile))
    for items in TECH.values():
        for slug,label in items:write('badges/'+slug+'.svg',badge(label))
    for slug,label in [('email','Email'),('repositories','All repositories'),('admin-source','Admin Panel / Code'),('chat-source','Chat App / Code'),('express-learning','Express.js · learning')]:write('badges/'+slug+'.svg',badge(label,True))
    if '--assets-only' not in sys.argv:
        (ROOT/'README.md').write_text(make_readme(),encoding='utf-8')

if __name__=='__main__':main()
