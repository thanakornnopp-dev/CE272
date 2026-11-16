# -*- coding: utf-8 -*-

def get_section_lab4():
    return r'''
<section id="lab4">
  <header class="top">
    <p class="kick">ปฏิบัติการที่ 4 · กฎการคงตัวของพลังงานและการไหลในท่อเวนจูรี่</p>
    <h1>บทที่ 4: สมการเบอร์นูลี่และการประยุกต์ใช้ (Bernoulli's Theorem)</h1>
    <p class="sub">Conservation of Energy · Venturi Tube · Energy Grade Line (EGL) · สัมประสิทธิ์การปรับแก้ Cd</p>
    <p class="by">CE 272 ปฏิบัติการกลศาสตร์ของไหล · ภาควิชาวิศวกรรมโยธา มหาวิทยาลัยธรรมศาสตร์</p>
    <p class="pracnote">โหมดฝึกเปิดอยู่: ซ่อนวิธีทำไว้ แตะแต่ละขั้นเพื่อดู (ลองเขียนเองก่อน) กดปุ่ม "ฝึก" อีกครั้งเพื่อปิด</p>
  </header>

  <h2 class="prob"><span class="tag">บทที่ 4</span>สมการเบอร์นูลี่และท่อเวนจูรี่</h2>
  <div class="stmt">
    <p>สมการเบอร์นูลี่เป็นหนึ่งในสมการที่สำคัญที่สุดในกลศาสตร์ของไหล อธิบายถึงการอนุรักษ์พลังงานกลของการไหล โดยนำสมการเบอร์นูลี่มาประยุกต์ใช้ร่วมกับสมการความต่อเนื่อง (Continuity Equation) ในหลอดเวนจูรี่ (Venturi Meter) เพื่อวัดอัตราการไหลในท่อปิดผ่านการตรวจวัดผลต่างของความดันระหว่างจุดทางเข้าและจุดคอคอด</p>
  </div>

  <div class="jump">
    <a href="#lab4-principle">ก. วัตถุประสงค์และสมการพลังงาน</a>
    <a href="#lab4-diagram">ข. อุปกรณ์และท่อเวนจูรี่</a>
    <a href="#lab4-eq">ค. สูตรและการหาค่า Cd</a>
    <a href="#lab4-traps">ง. จุดดักคะแนนข้อสอบ</a>
    <a href="#lab4-exam">จ. ตัวอย่างโจทย์ข้อสอบและการแสดงวิธีทำ</a>
  </div>

  <h3 class="grp" id="lab4-principle">ก. วัตถุประสงค์และสมการพลังงาน (First Principles)</h3>
  <p>ภายใต้สมมติฐานของไหลในอุดมคติ (Ideal Fluid: อัดตัวไม่ได้ ไม่มีความหนืด และไหลแบบคงตัว) การอินทิเกรตสมการการเคลื่อนที่ของออยเลอร์ (Euler's Equation) จะได้สมการเบอร์นูลี่:</p>
  
  $$\frac{P_1}{\gamma} + \frac{v_1^2}{2g} + z_1 = \frac{P_2}{\gamma} + \frac{v_2^2}{2g} + z_2 + h_f\tag{4.1}$$

  <ol class="st">
    <li><b>Pressure Head (\(\frac{P}{\gamma}\)):</b> เฮดความดัน วัดได้โดยตรงจากความสูงของลำน้ำในท่อมาโนมิเตอร์ [m]</li>
    <li><b>Velocity Head (\(\frac{v^2}{2g}\)):</b> เฮดความเร็ว เกิดจากพลังงานจลน์ของการไหล [m]</li>
    <li><b>Elevation Head (\(z\)):</b> เฮดระดับความสูงจากแนวระนาบอ้างอิง (Datum) [m]</li>
    <li><b>Energy Grade Line (EGL):</b> เส้นระดับพลังงานรวม \(\text{EGL} = \frac{P}{\gamma} + \frac{v^2}{2g} + z\)</li>
    <li><b>Hydraulic Grade Line (HGL):</b> เส้นระดับชลศาสตร์ \(\text{HGL} = \frac{P}{\gamma} + z\) (ระดับผิวน้ำในหลอดมาโนมิเตอร์)</li>
  </ol>

  <h3 class="grp" id="lab4-diagram">ข. แผนภาพหลอดเวนจูรี่และระดับน้ำในมาโนมิเตอร์</h3>
  <figure>
    <svg viewBox="0 0 680 280" role="img" aria-label="ท่อเวนจูรี่และหลอดแก้วมาโนมิเตอร์แสดงระดับความดัน">
      <!-- Venturi Tube Outline -->
      <path d="M 60 160 L 220 160 L 320 190 L 360 190 L 520 160 L 620 160" fill="none" stroke="var(--ink)" stroke-width="2.5"/>
      <path d="M 60 220 L 220 220 L 320 210 L 360 210 L 520 220 L 620 220" fill="none" stroke="var(--ink)" stroke-width="2.5"/>
      
      <!-- Water flow area -->
      <path d="M 60 160 L 220 160 L 320 190 L 360 190 L 520 160 L 620 160 L 620 220 L 520 220 L 360 210 L 320 210 L 220 220 L 60 220 Z" fill="var(--water)" opacity="0.5"/>

      <!-- Manometer tubes -->
      <!-- Tube 1 (Inlet, wide, high pressure) -->
      <line x1="160" y1="160" x2="160" y2="40" stroke="var(--ink)" stroke-width="1.5"/>
      <line x1="172" y1="160" x2="172" y2="40" stroke="var(--ink)" stroke-width="1.5"/>
      <rect x="161" y="70" width="10" height="90" fill="var(--blue)" opacity="0.7"/>
      <text x="166" y="32" font-size="12" font-weight="700" text-anchor="middle" fill="var(--navy)">h1</text>
      <text x="166" y="240" font-size="13" font-weight="600" text-anchor="middle" fill="var(--navy)">จุด 1 (ทางเข้า)</text>

      <!-- Tube 2 (Throat, narrow, low pressure!) -->
      <line x1="334" y1="190" x2="334" y2="40" stroke="var(--ink)" stroke-width="1.5"/>
      <line x1="346" y1="190" x2="346" y2="40" stroke="var(--ink)" stroke-width="1.5"/>
      <rect x="335" y="140" width="10" height="50" fill="var(--blue)" opacity="0.7"/>
      <text x="340" y="32" font-size="12" font-weight="700" text-anchor="middle" fill="var(--red)">h2 (ต่ำสุด!)</text>
      <text x="340" y="240" font-size="13" font-weight="600" text-anchor="middle" fill="var(--red)">จุด 2 (คอคอด Throat)</text>

      <!-- Tube 3 (Diverging outlet, partial recovery) -->
      <line x1="560" y1="160" x2="560" y2="40" stroke="var(--ink)" stroke-width="1.5"/>
      <line x1="572" y1="160" x2="572" y2="40" stroke="var(--ink)" stroke-width="1.5"/>
      <rect x="561" y="90" width="10" height="70" fill="var(--blue)" opacity="0.7"/>
      <text x="566" y="32" font-size="12" font-weight="700" text-anchor="middle" fill="var(--navy)">h3</text>
      <text x="566" y="240" font-size="13" font-weight="600" text-anchor="middle" fill="var(--navy)">จุด 3 (ทางออก)</text>

      <!-- Flow Arrow -->
      <line x1="70" y1="190" x2="120" y2="190" stroke="var(--blue)" stroke-width="2.5" marker-end="url(#ar)"/>
      <text x="95" y="180" font-size="12" fill="var(--blue)" text-anchor="middle">ทิศทางการไหล</text>

      <!-- Δh indicator -->
      <line x1="175" y1="70" x2="330" y2="70" stroke="var(--red)" stroke-width="1" stroke-dasharray="3 3"/>
      <line x1="350" y1="70" x2="350" y2="140" stroke="var(--red)" stroke-width="1.5" marker-start="url(#ar)" marker-end="url(#ar)"/>
      <text x="365" y="110" font-size="13" font-weight="700" fill="var(--red)">Δh = h1 - h2</text>
    </svg>
    <figcaption>รูปที่ 4.1 ระดับน้ำในหลอดมาโนมิเตอร์ตามความยาวของท่อเวนจูรี่ (คอคอดความเร็วสูงสุดแต่ความดันต่ำสุด)</figcaption>
  </figure>

  <h3 class="grp" id="lab4-eq">ค. สูตรและการคำนวณหาค่าสัมประสิทธิ์ Cd</h3>
  <p>สำหรับท่อที่วางอยู่ในแนวระดับ (\(z_1 = z_2\)) และสมมติยังไม่คิดการสูญเสียพลังงาน (\(h_f = 0\)):</p>
  
  $$h_1 + \frac{v_1^2}{2g} = h_2 + \frac{v_2^2}{2g}\tag{4.2}$$

  <p>จากสมการความต่อเนื่อง \(v_1 A_1 = v_2 A_2 \Rightarrow v_2 = v_1 \left(\frac{A_1}{A_2}\right)\) แทนค่าลงในสมการจะได้ความเร็วและอัตราการไหลทางทฤษฎีคือ:</p>
  
  $$v_1 = \sqrt{\frac{2g(h_1 - h_2)}{(A_1/A_2)^2 - 1}}\tag{4.6}$$
  $$Q_{\text{theory}} = A_1 \sqrt{\frac{2g(h_1 - h_2)}{(A_1/A_2)^2 - 1}}\tag{4.7}$$

  <p>ในความเป็นจริงย่อมมีการสูญเสียพลังงานจากความเสียดทานและการหมุนวน อัตราการไหลจริง (\(Q_{\text{act}}\)) จึงน้อยกว่าทฤษฎีเล็กน้อย สัมประสิทธิ์การปรับแก้ (Discharge Coefficient, \(C_d\)) หาได้จาก:</p>
  
  $$C_d = \frac{Q_{\text{actual}}}{Q_{\text{theory}}}\tag{4.9}$$

  <h3 class="grp" id="lab4-traps">ง. จุดดักคะแนนข้อสอบ</h3>
  <div class="bx trap">
    <b>กับดักความเข้าใจเรื่องความดันที่คอคอด (The Venturi Paradox):</b>
    <div>
      นักศึกษามักเข้าใจผิดว่า <i>"จุดที่ท่อบีบแคบลง น้ำจะอัดแน่น ความดันจึงต้องสูงขึ้น"</i> ซึ่ง <b>ผิดมหันต์!</b><br>
      • ตามกฎอนุรักษ์พลังงานเบอร์นูลี่ พลังงานรวมมีค่าคงที่ เมื่อหน้าตัดแคบลง น้ำต้องเร่งความเร็ว (\(v\) สูงขึ้นมาก)<br>
      • ส่งผลให้พลังงานจลน์ (\(\frac{v^2}{2g}\)) เพิ่มขึ้นอย่างมหาศาล<br>
      • พลังงานศักย์ของความดัน (\(\frac{P}{\gamma}\)) จึง <b>ต้องลดฮวบลงต่ำที่สุด</b> เพื่อรักษาสมดุลพลังงานรวม!
    </div>
  </div>

  <div class="bx chk">
    <b>ข้อควรระวังในห้องแล็บ:</b>
    <div>
      • ต้องไล่ฟองอากาศออกจากท่อมาโนมิเตอร์ให้หมดก่อนเริ่มบันทึกข้อมูล มิฉะนั้นระดับน้ำจะอ่านเพี้ยน<br>
      • ค่า \(C_d\) ของท่อเวนจูรี่ที่ดีจะอยู่ในช่วง \(0.95 - 0.98\) เสมอ
    </div>
  </div>

  <h3 class="grp" id="lab4-exam">จ. ตัวอย่างโจทย์ข้อสอบและการแสดงวิธีทำ (Exam Practice)</h3>
  <div class="stmt">
    <p><b>โจทย์ตัวอย่าง:</b> ท่อเวนจูรี่มีเส้นผ่านศูนย์กลางทางเข้า \(D_1 = 26\text{ mm}\) และคอคอด \(D_2 = 16\text{ mm}\) เมื่อน้ำไหลผ่าน อ่านผลต่างของระดับน้ำในมาโนมิเตอร์ได้ \(h_1 - h_2 = 18.5\text{ cm}\) ตวงน้ำที่ทางออกได้ปริมาตร \(10\text{ L}\) ในเวลา \(29.4\text{ s}\) จงหา (ก) อัตราการไหลทางทฤษฎี \(Q_{\text{th}}\) (ข) อัตราการไหลจริง \(Q_{\text{act}}\) และ (ค) สัมประสิทธิ์การปรับแก้ \(C_d\)</p>
  </div>

  <h4 class="cardt">เฉลยวิธีทำ (เขียนส่งอาจารย์ตามลำดับ)</h4>
  <div class="exam">
    <div class="row">
      <div class="lab">ข้อมูลที่กำหนด</div>
      <div class="given">$$\begin{aligned} & D_1 = 0.026\ \text{m},\quad D_2 = 0.016\ \text{m} \\ & h_1 - h_2 = 0.185\ \text{m} \\ & V = 10\ \text{L} = 0.010\ \text{m}^3,\quad t = 29.4\ \text{s} \end{aligned}$$</div>
    </div>
    <div class="row">
      <div class="lab">พื้นที่หน้าตัด</div>
      <div>$$\begin{aligned} A_1 &= \frac{\pi(0.026)^2}{4} = 5.3093 \times 10^{-4}\ \text{m}^2 \\ A_2 &= \frac{\pi(0.016)^2}{4} = 2.0106 \times 10^{-4}\ \text{m}^2 \\ \frac{A_1}{A_2} &= \left(\frac{26}{16}\right)^2 = 2.6406,\quad \left(\frac{A_1}{A_2}\right)^2 = 6.973 \end{aligned}$$</div>
    </div>
    <div class="row">
      <div class="lab">(ก) Q ทางทฤษฎี</div>
      <div>$$\begin{aligned} v_1 &= \sqrt{\frac{2(9.81)(0.185)}{6.973 - 1}} = \sqrt{\frac{3.6297}{5.973}} = 0.7796\ \text{m/s} \\ Q_{\text{th}} &= A_1 v_1 = (5.3093 \times 10^{-4})(0.7796) = 4.139 \times 10^{-4}\ \text{m}^3/\text{s} \end{aligned}$$</div>
    </div>
    <div class="row">
      <div class="lab">(ข) Q จริง</div>
      <div>$$Q_{\text{act}} = \frac{\Delta V}{\Delta t} = \frac{0.010\ \text{m}^3}{29.4\ \text{s}} = 3.401 \times 10^{-4}\ \text{m}^3/\text{s}$$</div>
    </div>
    <div class="row">
      <div class="lab">(ค) สัมประสิทธิ์ Cd</div>
      <div>$$C_d = \frac{Q_{\text{act}}}{Q_{\text{th}}} = \frac{3.401 \times 10^{-4}}{4.139 \times 10^{-4}} = 0.8217\quad (\text{สมเหตุสมผล})$$</div>
    </div>
    <div class="row">
      <div class="lab">คำตอบสุดท้าย</div>
      <div><span class="fin">\(Q_{\text{th}} = 4.14 \times 10^{-4}\ \text{m}^3/\text{s},\quad Q_{\text{act}} = 3.40 \times 10^{-4}\ \text{m}^3/\text{s},\quad C_d = 0.822\)</span></div>
    </div>
  </div>

  <div class="pn">
    <a href="#lab3">← บทที่ 3 แรงกระแทกลำน้ำ</a>
    <a href="#lab5">บทที่ 5 สมการแมนนิ่ง →</a>
  </div>
</section>
'''
