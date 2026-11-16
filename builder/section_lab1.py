# -*- coding: utf-8 -*-

def get_section_lab1():
    return r'''
<section id="lab1">
  <header class="top">
    <p class="kick">ปฏิบัติการที่ 1 · พื้นฐานการวัดอัตราการไหลและการจ่ายน้ำ</p>
    <h1>บทที่ 1: โต๊ะชลศาสตร์ (Hydraulic Bench)</h1>
    <p class="sub">ส่วนประกอบโต๊ะชลศาสตร์ · การวัดอัตราการไหลจริงโดยวิธีปริมาตรต่อเวลา · การแปลงหน่วย SI</p>
    <p class="by">CE 272 ปฏิบัติการกลศาสตร์ของไหล · ภาควิชาวิศวกรรมโยธา มหาวิทยาลัยธรรมศาสตร์</p>
    <p class="pracnote">โหมดฝึกเปิดอยู่: ซ่อนวิธีทำไว้ แตะแต่ละขั้นเพื่อดู (ลองเขียนเองก่อน) กดปุ่ม "ฝึก" อีกครั้งเพื่อปิด</p>
  </header>

  <h2 class="prob"><span class="tag">บทที่ 1</span>หลักการทำงานและการวัดอัตราการไหล</h2>
  <div class="stmt">
    <p>โต๊ะชลศาสตร์ (Hydraulic Bench) เป็นอุปกรณ์หลักในห้องปฏิบัติการกลศาสตร์ของไหล ทำหน้าที่เป็น <b>สถานีจ่ายน้ำหมุนเวียน (Closed-loop Water Supply)</b> และ <b>อุปกรณ์วัดอัตราการไหลจริง (Actual Flow Rate Measurement)</b> ให้กับชุดทดลองอื่นๆ ในห้องปฏิบัติการเกือบทั้งหมด (เช่น จุดศูนย์กลางแรงดัน, ลำน้ำพุ่งชนฉาก, ท่อเบอร์นูลี่, การไหลผ่านฝาย, การไหลผ่านรูลอด)</p>
  </div>

  <div class="jump">
    <a href="#lab1-principle">ก. วัตถุประสงค์และหลักการ</a>
    <a href="#lab1-diagram">ข. อุปกรณ์และแผนผังการไหล</a>
    <a href="#lab1-eq">ค. สูตรและการคำนวณ</a>
    <a href="#lab1-traps">ง. จุดดักคะแนนข้อสอบ</a>
    <a href="#lab1-exam">จ. ตัวอย่างโจทย์และวิธีทำ</a>
  </div>

  <h3 class="grp" id="lab1-principle">ก. วัตถุประสงค์และหลักการ First Principles</h3>
  <p>ในวิศวกรรมชลศาสตร์ การวัดอัตราการไหลของของเหลวที่มีความแม่นยำและเป็นค่าอ้างอิงพื้นฐานที่สุด (Primary Standard) คือ <b>วิธีวัดปริมาตรเทียบกับเวลา (Volumetric Method)</b> เพราะของเหลวมีคุณสมบัติอัดตัวไม่ได้ (Incompressible Fluid) ปริมาตรที่กักเก็บได้ในถังตวงจึงเท่ากับผลรวมของอัตราการไหลสะสมในช่วงเวลานั้น</p>
  
  <h3 class="grp" id="lab1-diagram">ข. ส่วนประกอบหลักของโต๊ะชลศาสตร์</h3>
  <ol class="st">
    <li><b>ถังเก็บน้ำด้านล่าง (Sump Tank):</b> อ่างเก็บน้ำหลักสำหรับจ่ายน้ำหมุนเวียนในระบบ ป้องกันไม่ให้น้ำสูญหาย</li>
    <li><b>เครื่องสูบน้ำ (Centrifugal Pump):</b> สูบน้ำจากถังพักด้านล่าง ส่งขึ้นไปยังชุดทดลองด้านบน</li>
    <li><b>ถังตวงน้ำด้านบน (Volumetric Tank):</b> ถังรูปทรงเรขาคณิตสำหรับรองรับน้ำที่ไหลออกจากชุดทดลองเพื่อวัดปริมาตร</li>
    <li><b>วาล์วดิ่งระบายน้ำ (Drain / Dump Valve):</b> วาล์วยกดิ่งก้นถังตวง เมื่อปิดวาล์วน้ำจะสะสมในถังตวง เมื่อเปิดวาล์วน้ำจะระบายกลับลงสู่ถังพักด้านล่าง</li>
    <li><b>หลอดแก้ววัดระดับน้ำ (Sight Glass):</b> หลอดแก้วใสติดสเกลด้านข้างโต๊ะ แสดงระดับน้ำในถังตวงเป็นหน่วยลิตร (L)</li>
    <li><b>พื้นที่ติดตั้งอุปกรณ์เสริม (Working Surface):</b> รางวางชุดอุปกรณ์ทดสอบต่างๆ</li>
  </ol>

  <figure>
    <svg viewBox="0 0 680 320" role="img" aria-label="แผนภาพจำลองโต๊ะชลศาสตร์และการไหลวนของน้ำ">
      <!-- Sump Tank -->
      <rect x="140" y="210" width="400" height="90" fill="var(--hover)" stroke="var(--ink)" stroke-width="2"/>
      <rect x="142" y="235" width="396" height="63" fill="var(--water)" opacity="0.6"/>
      <text x="340" y="265" font-size="16" font-weight="600" text-anchor="middle" fill="var(--navy)">ถังเก็บน้ำด้านล่าง (Sump Tank)</text>
      
      <!-- Volumetric Tank -->
      <rect x="200" y="70" width="280" height="90" fill="var(--hover)" stroke="var(--ink)" stroke-width="2"/>
      <rect x="202" y="105" width="276" height="53" fill="var(--water)" opacity="0.8"/>
      <text x="340" y="125" font-size="15" font-weight="600" text-anchor="middle" fill="var(--navy)">ถังตวงปริมาตร (Volumetric Tank)</text>

      <!-- Sight Glass -->
      <rect x="495" y="65" width="22" height="100" fill="var(--bg)" stroke="var(--ink)" stroke-width="1.5"/>
      <line x1="500" y1="85" x2="512" y2="85" stroke="var(--gold)" stroke-width="1.5"/>
      <line x1="500" y1="105" x2="512" y2="105" stroke="var(--gold)" stroke-width="1.5"/>
      <line x1="500" y1="125" x2="512" y2="125" stroke="var(--gold)" stroke-width="1.5"/>
      <line x1="500" y1="145" x2="512" y2="145" stroke="var(--gold)" stroke-width="1.5"/>
      <text x="530" y="120" font-size="13" fill="var(--gray)">Sight Glass สเกลลิตร</text>

      <!-- Dump Valve -->
      <line x1="340" y1="160" x2="340" y2="210" stroke="var(--red)" stroke-width="4" stroke-dasharray="4 2"/>
      <circle cx="340" cy="185" r="7" fill="var(--red)"/>
      <text x="355" y="190" font-size="13" font-weight="600" fill="var(--red)">วาล์วดิ่งระบายน้ำ (Dump Valve)</text>

      <!-- Pump & Pipe -->
      <circle cx="70" cy="255" r="24" fill="var(--bg)" stroke="var(--navy)" stroke-width="2.5"/>
      <text x="70" y="260" font-size="12" font-weight="700" text-anchor="middle" fill="var(--navy)">PUMP</text>
      <!-- Suction pipe -->
      <path d="M140 260 H94" fill="none" stroke="var(--navy)" stroke-width="3" marker-end="url(#ar)"/>
      <!-- Discharge pipe -->
      <path d="M70 231 V35 H340 V65" fill="none" stroke="var(--blue)" stroke-width="3" marker-end="url(#ar)"/>
      <text x="180" y="25" font-size="13" fill="var(--blue)">น้ำส่งขึ้นชุดทดลองด้านบน</text>
    </svg>
    <figcaption>รูปที่ 1.1 วงจรการไหลและการตวงปริมาตรบนโต๊ะชลศาสตร์ (Hydraulic Bench Flow Loop)</figcaption>
  </figure>

  <h3 class="grp" id="lab1-eq">ค. สูตรและการคำนวณอัตราการไหล</h3>
  <p>เมื่อปิดวาล์วดิ่ง (Dump Valve) เพื่อกักน้ำไว้ในถังตวง ให้นักศึกษาอ่านระดับปริมาตรน้ำเริ่มต้น \(\text{Volume}_1\) พร้อมกดเริ่มจับเวลา \(t_1\) เมื่อระดับน้ำสูงขึ้นถึงระดับที่ต้องการให้อ่านปริมาตรสิ้นสุด \(\text{Volume}_2\) และหยุดเวลา \(t_2\)</p>
  
  $$Q_{\text{actual}} = \frac{\Delta V}{\Delta t} = \frac{\text{Volume}_2 - \text{Volume}_1}{\text{Time}_2 - \text{Time}_1}\tag{1.1}$$

  <div class="plan">
    <p><b class="l">ขั้นที่ 1:</b> คำนวณผลต่างปริมาตร \(\Delta V = V_2 - V_1\) (หากอ่านเป็นลิตร ให้แปลงเป็น \(\text{m}^3\) โดยคูณ \(10^{-3}\))</p>
    <p><b class="l">ขั้นที่ 2:</b> คำนวณช่วงเวลาที่ใช้ \(\Delta t = t_2 - t_1\) [วินาที]</p>
    <p><b class="l">ขั้นที่ 3:</b> นำ \(\Delta V\) หารด้วย \(\Delta t\) ได้อัตราการไหลจริงในหน่วย SI คือ \(\text{m}^3/\text{s}\)</p>
  </div>

  <h3 class="grp" id="lab1-traps">ง. จุดดักคะแนนและข้อควรระวังในห้องสอบ</h3>
  <div class="bx trap">
    <b>ข้อผิดพลาดอันดับ 1: ลืมแปลงหน่วยปริมาตร</b>
    <div>
      สเกลบนหลอดแก้ว Sight glass แสดงค่าเป็น <b>ลิตร (L)</b> เสมอ<br>
      • \(1\text{ L} = 10^{-3}\text{ m}^3 = 0.001\text{ m}^3\)<br>
      • \(1\text{ mL} = 10^{-6}\text{ m}^3\)<br>
      ถ้าคำนวณ \(Q = 20/40 = 0.5\) แล้วตอบ \(0.5\text{ m}^3/\text{s}\) จะผิดทันทีเพราะค่าจริงคือ \(0.5\text{ L/s} = 5 \times 10^{-4}\text{ m}^3/\text{s}\)
    </div>
  </div>

  <div class="bx chk">
    <b>ข้อแนะนำในการทำแล็บจริง:</b>
    <div>
      ควรรอให้ระดับน้ำในถังตวงลอยพ้นช่วงระดับต่ำสุดก่อนเริ่มกดจับเวลา (เช่น เริ่มจับเวลาที่ \(5\text{ L}\) ถึง \(25\text{ L}\)) เพื่อลดความคลาดเคลื่อนจากความผันผวนของผิวน้ำที่เริ่มสะสมตัว
    </div>
  </div>

  <h3 class="grp" id="lab1-exam">จ. ตัวอย่างโจทย์ข้อสอบและการแสดงวิธีทำ (Exam Practice)</h3>
  <div class="stmt">
    <p><b>โจทย์ตัวอย่าง:</b> ในการทดสอบอัตราการไหลด้วยโต๊ะชลศาสตร์ ปิดวาล์วดิ่งแล้วเริ่มจับเวลาเมื่อระดับน้ำในหลอดแก้วอยู่ที่ \(5\text{ L}\) จนกระทั่งระดับน้ำขึ้นไปถึง \(35\text{ L}\) นาฬิกาจับเวลาอ่านได้ \(48.5\text{ s}\) จงหาอัตราการไหลจริงของน้ำในหน่วย (ก) \(\text{L/s}\) (ข) \(\text{m}^3/\text{s}\) และ (ค) \(\text{m}^3/\text{hr}\)</p>
  </div>

  <h4 class="cardt">เฉลยวิธีทำ (เขียนส่งอาจารย์ตามลำดับ)</h4>
  <div class="exam">
    <div class="row">
      <div class="lab">ข้อมูลที่กำหนด</div>
      <div class="given">$$\begin{aligned} & V_1 = 5\ \text{L},\quad V_2 = 35\ \text{L} \\ & \Delta t = 48.5\ \text{s} \end{aligned}$$</div>
    </div>
    <div class="row">
      <div class="lab">(ก) Q ในหน่วย L/s</div>
      <div>$$\Delta V = 35 - 5 = 30\ \text{L}$$$$Q = \frac{\Delta V}{\Delta t} = \frac{30\ \text{L}}{48.5\ \text{s}} = 0.6186\ \text{L/s}$$</div>
    </div>
    <div class="row">
      <div class="lab">(ข) Q ในหน่วย SI (m³/s)</div>
      <div>$$\Delta V = 30 \times 10^{-3}\ \text{m}^3$$$$Q = \frac{30 \times 10^{-3}\ \text{m}^3}{48.5\ \text{s}} = 6.186 \times 10^{-4}\ \text{m}^3/\text{s}\quad \htmlClass{ok}{(\text{OK})}$$</div>
    </div>
    <div class="row">
      <div class="lab">(ค) Q ในหน่วย m³/hr</div>
      <div>$$Q = (6.186 \times 10^{-4}\ \text{m}^3/\text{s}) \times 3600\ \text{s/hr} = 2.227\ \text{m}^3/\text{hr}$$</div>
    </div>
    <div class="row">
      <div class="lab">คำตอบสุดท้าย</div>
      <div><span class="fin">\(Q = 0.619\ \text{L/s} = 6.19 \times 10^{-4}\ \text{m}^3/\text{s} = 2.23\ \text{m}^3/\text{hr}\)</span></div>
    </div>
  </div>

  <div class="pn">
    <a href="#sum">← สรุปภาพรวม</a>
    <a href="#lab2">บทที่ 2 จุดศูนย์กลางของแรงดัน →</a>
  </div>
</section>
'''
