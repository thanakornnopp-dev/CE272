# -*- coding: utf-8 -*-

def get_section_lab8():
    return r'''
<section id="lab8">
  <header class="top">
    <p class="kick">ปฏิบัติการที่ 8 · การหดตัวของลำน้ำและวิถีการเคลื่อนที่แบบโพรเจกไทล์</p>
    <h1>บทที่ 8: การไหลผ่านรูลอด (Flow through Orifice)</h1>
    <p class="sub">Vena Contracta · สัมประสิทธิ์ 3 ตัว (Cv, Cc, Cd) · การพิสูจน์วิถีลำน้ำ Jet Trajectory</p>
    <p class="by">CE 272 ปฏิบัติการกลศาสตร์ของไหล · ภาควิชาวิศวกรรมโยธา มหาวิทยาลัยธรรมศาสตร์</p>
    <p class="pracnote">โหมดฝึกเปิดอยู่: ซ่อนวิธีทำไว้ แตะแต่ละขั้นเพื่อดู (ลองเขียนเองก่อน) กดปุ่ม "ฝึก" อีกครั้งเพื่อปิด</p>
  </header>

  <h2 class="prob"><span class="tag">บทที่ 8</span>รูลอดขอบคมและแนวเส้นทางเดินของลำน้ำ</h2>
  <div class="stmt">
    <p>การศึกษาการไหลผ่านรูลอดขนาดเล็กขอบคม (Sharp-edged Orifice) เป็นพื้นฐานในการทำความเข้าใจพฤติกรรมการบีบตัวของสายน้ำ (Streamlines Convergence) การสูญเสียพลังงานเนื่องจากความหนืด และการนำสมการวิถีโพรเจกไทล์ (Projectile Motion) มาตรวจวัดความเร็วจริงของลำน้ำที่พุ่งออกมาอย่างอิสระ</p>
  </div>

  <div class="jump">
    <a href="#lab8-theory">ก. วัตถุประสงค์และสัมประสิทธิ์ 3 ตัว</a>
    <a href="#lab8-trajectory">ข. การพิสูจน์สมการวิถีลำน้ำ</a>
    <a href="#lab8-diagram">ค. อุปกรณ์และชุดเข็มวัดพิกัด</a>
    <a href="#lab8-traps">ง. จุดดักคะแนนข้อสอบ</a>
    <a href="#lab8-exam">จ. ตัวอย่างโจทย์ข้อสอบและการแสดงวิธีทำ</a>
  </div>

  <h3 class="grp" id="lab8-theory">ก. วัตถุประสงค์และสัมประสิทธิ์ไฮดรอลิก 3 ตัว</h3>
  <p>เมื่อน้ำไหลออกจากถังที่มีระดับความสูงคงที่ \(H\) ผ่านรูเจาะขอบคม ความเร็วตามทฤษฎีของทอร์ริเชลลีคือ \(v_{\text{th}} = \sqrt{2gH}\) และอัตราการไหลทฤษฎีคือ \(Q_{\text{th}} = A_0 \sqrt{2gH}\) โดย \(A_0 = \frac{\pi d_0^2}{4}\)</p>
  
  <p>เนื่องจากสายน้ำที่พุ่งเข้าหารูเจาะจากทุกทิศทางมีความเฉื่อย ลำน้ำจึงบีบตัวเล็กลงจนมีหน้าตัดแคบที่สุดที่จุด <b>เวนา คอนแทรกตา (Vena Contracta)</b> ซึ่งอยู่ห่างจากปากรูเจาะประมาณ \(d_0/2\) ทำให้เกิดสัมประสิทธิ์ 3 ตัว:</p>

  <div class="tw">
    <table>
      <caption>นิยามและความสัมพันธ์ของสัมประสิทธิ์ไฮดรอลิกทั้ง 3 ตัว</caption>
      <thead>
        <tr><th>สัมประสิทธิ์</th><th>สัญลักษณ์</th><th>สูตรการคำนวณ</th><th>ช่วงค่าปกติในห้องแล็บ</th></tr>
      </thead>
      <tbody>
        <tr>
          <td><b>1. สัมประสิทธิ์ความเร็ว</b> (Velocity)</td>
          <td>\(C_v\)</td>
          <td>\(C_v = \frac{v_{\text{actual}}}{v_{\text{theoretical}}} = \frac{v_{\text{act}}}{\sqrt{2gH}}\)</td>
          <td>\(0.95 - 0.98\) (ความฝืดน้อย)</td>
        </tr>
        <tr>
          <td><b>2. สัมประสิทธิ์การหดตัว</b> (Contraction)</td>
          <td>\(C_c\)</td>
          <td>\(C_c = \frac{A_c}{A_0} = \left(\frac{d_c}{d_0}\right)^2\)</td>
          <td>\(0.62 - 0.65\) (หดตัวสูง)</td>
        </tr>
        <tr>
          <td><b>3. สัมประสิทธิ์การไหล</b> (Discharge)</td>
          <td>\(C_d\)</td>
          <td>\(C_d = C_v \times C_c = \frac{Q_{\text{actual}}}{Q_{\text{theoretical}}}\)</td>
          <td>\(0.60 - 0.63\)</td>
        </tr>
      </tbody>
    </table>
  </div>

  <h3 class="grp" id="lab8-trajectory">ข. การพิสูจน์สมการวิถีลำน้ำ (Jet Trajectory Proof)</h3>
  <p>ลำน้ำที่พุ่งออกจากรูลอดจะเคลื่อนที่แบบโพรเจกไทล์ภายใต้แรงโน้มถ่วงโลก กำหนดจุดกำเนิด \((0,0)\) อยู่ที่กึ่งกลางรูลอด:</p>
  <ol class="st">
    <li><b>แนวราบ (แกน X):</b> ไม่มีความเร่ง (\(a_x = 0\)) ลำน้ำวิ่งด้วยความเร็วจริงคงที่:
      $$x = v_{\text{actual}} \cdot t \Rightarrow t = \frac{x}{v_{\text{actual}}}\tag{8.15}$$
    </li>
    <li><b>แนวดิ่ง (แกน Y):</b> ตกอิสระใต้แรงโน้มถ่วง (\(a_y = g\)) ความเร็วต้นแนวดิ่งเป็นศูนย์:
      $$y = \frac{1}{2}gt^2 \Rightarrow t = \sqrt{\frac{2y}{g}}\tag{8.19}$$
    </li>
    <li><b>รวมสมการเพื่อกำจัดเวลา \(t\):</b>
      $$x = v_{\text{actual}} \sqrt{\frac{2y}{g}} = \left(C_v \sqrt{2gH}\right) \sqrt{\frac{2y}{g}} = 2 C_v \sqrt{yH}\tag{8.22}$$
    </li>
  </ol>

  <p><b>การวิเคราะห์กราฟ:</b> เมื่อเขียนกราฟระหว่างระยะตกราบ \(x\) (แกน Y) กับ \(\sqrt{yH}\) (แกน X) จะได้เส้นตรงผ่านจุดกำเนิดที่มี:</p>
  $$\text{Slope} = 2 C_v \Rightarrow C_v = \frac{\text{Slope}}{2}$$

  <h3 class="grp" id="lab8-diagram">ค. อุปกรณ์และชุดเข็มวัดพิกัดลำน้ำ</h3>
  <figure>
    <svg viewBox="0 0 680 260" role="img" aria-label="ถังน้ำและวิถีลำน้ำพุ่งผ่านชุดเข็มวัดพิกัด">
      <!-- Water Tank Left -->
      <rect x="60" y="30" width="100" height="200" fill="var(--hover)" stroke="var(--ink)" stroke-width="2"/>
      <rect x="62" y="60" width="96" height="168" fill="var(--water)" opacity="0.6"/>
      <line x1="50" y1="60" x2="170" y2="60" stroke="var(--blue)" stroke-width="2"/>
      <text x="110" y="50" font-size="13" font-weight="600" text-anchor="middle" fill="var(--blue)">ผิวน้ำ H</text>

      <!-- Orifice opening -->
      <rect x="155" y="165" width="10" height="20" fill="var(--bg)"/>
      <circle cx="160" cy="175" r="4" fill="var(--red)"/>
      <text x="110" y="180" font-size="12" font-weight="700" text-anchor="middle" fill="var(--red)">รูลอด Orifice</text>

      <!-- Head H dimension -->
      <line x1="40" y1="60" x2="40" y2="175" stroke="var(--navy)" stroke-width="1.5" marker-start="url(#ar)" marker-end="url(#ar)"/>
      <text x="30" y="120" font-size="13" font-weight="700" text-anchor="end" fill="var(--navy)">H</text>

      <!-- Parabolic Jet Path -->
      <path d="M 160 175 Q 320 180 580 250" fill="none" stroke="var(--blue)" stroke-width="3"/>
      
      <!-- Needles Gauges -->
      <g stroke="var(--ink)" stroke-width="1.5">
        <line x1="220" y1="120" x2="220" y2="178"/>
        <line x1="280" y1="120" x2="280" y2="183"/>
        <line x1="360" y1="120" x2="360" y2="195"/>
        <line x1="440" y1="120" x2="440" y2="212"/>
        <line x1="520" y1="120" x2="520" y2="235"/>
      </g>
      <!-- Needles Header -->
      <line x1="200" y1="120" x2="540" y2="120" stroke="var(--gold)" stroke-width="3"/>
      <text x="370" y="110" font-size="13" font-weight="600" text-anchor="middle" fill="var(--gold)">ชุดเข็มวัดพิกัดวิถีลำน้ำ (Needle Probes)</text>

      <!-- Coordinate x and y -->
      <line x1="160" y1="150" x2="360" y2="150" stroke="var(--navy)" stroke-width="1.5" marker-end="url(#ar)"/>
      <text x="260" y="142" font-size="12" fill="var(--navy)">ระยะ x</text>
      <line x1="360" y1="175" x2="360" y2="195" stroke="var(--red)" stroke-width="1.5" marker-end="url(#ar)"/>
      <text x="370" y="188" font-size="12" fill="var(--red)">y</text>
    </svg>
    <figcaption>รูปที่ 8.1 การวัดแนววิถีลำน้ำด้วยชุดเข็มปรับระดับพิกัด \((x, y)\) เทียบกับเฮดน้ำ \(H\)</figcaption>
  </figure>

  <h3 class="grp" id="lab8-traps">ง. จุดดักคะแนนข้อสอบ</h3>
  <div class="bx trap">
    <b>กับดักความสัมพันธ์ \(C_d = C_v \times C_c\):</b>
    <div>
      • ค่า \(C_v \approx 0.97\) สูงมากเพราะการสูญเสียความหนืดมีน้อย<br>
      • แต่ค่า \(C_d \approx 0.62\) มีค่าต่ำ <b>เนื่องมาจาก \(C_c \approx 0.64\) (การหดตัวของพื้นที่หน้าตัด)</b> ไม่ใช่เพราะความเสียดทาน!<br>
      • ข้อสอบชอบถามว่า <i>"ทำไมอัตราการไหลจริงถึงลดลงเกือบ 40% ทั้งที่ความเร็วแทบไม่ลดลง?"</i> คำตอบคือ เกิดจากการหดตัวของลำน้ำที่ Vena Contracta
    </div>
  </div>

  <h3 class="grp" id="lab8-exam">จ. ตัวอย่างโจทย์ข้อสอบและการแสดงวิธีทำ (Exam Practice)</h3>
  <div class="stmt">
    <p><b>โจทย์ตัวอย่าง:</b> รูลอดขอบคมขนาดเส้นผ่านศูนย์กลาง \(d_0 = 10\text{ mm}\) ติดตั้งที่ข้างถังน้ำที่มีเฮดคงที่ \(H = 400\text{ mm}\) จากการวัดพิกัดลำน้ำ พบว่าที่ระยะตกราบ \(x = 350\text{ mm}\) ลำน้ำตกลงมาในแนวดิ่งเป็นระยะ \(y = 80\text{ mm}\) และวัดเส้นผ่านศูนย์กลางที่ Vena Contracta ได้ \(d_c = 8.0\text{ mm}\) จงหา (ก) สัมประสิทธิ์ความเร็ว \(C_v\) (ข) สัมประสิทธิ์การหดตัว \(C_c\) และ (ค) สัมประสิทธิ์อัตราการไหล \(C_d\)</p>
  </div>

  <h4 class="cardt">เฉลยวิธีทำ (เขียนส่งอาจารย์ตามลำดับ)</h4>
  <div class="exam">
    <div class="row">
      <div class="lab">ข้อมูลที่กำหนด</div>
      <div class="given">$$\begin{aligned} & H = 0.400\ \text{m},\quad d_0 = 0.010\ \text{m} \\ & x = 0.350\ \text{m},\quad y = 0.080\ \text{m} \\ & d_c = 0.008\ \text{m} \end{aligned}$$</div>
    </div>
    <div class="row">
      <div class="lab">(ก) สัมประสิทธิ์ Cv</div>
      <div>$$\begin{aligned} x &= 2 C_v \sqrt{yH} \\ 0.350 &= 2 C_v \sqrt{(0.080)(0.400)} = 2 C_v \sqrt{0.032} = 2 C_v (0.17888) = 0.35777 C_v \\ C_v &= \frac{0.350}{0.35777} = 0.9783\quad \htmlClass{ok}{(\text{ปกติ 0.95-0.98})} \end{aligned}$$</div>
    </div>
    <div class="row">
      <div class="lab">(ข) สัมประสิทธิ์ Cc</div>
      <div>$$C_c = \frac{A_c}{A_0} = \left(\frac{d_c}{d_0}\right)^2 = \left(\frac{8.0\ \text{mm}}{10.0\ \text{mm}}\right)^2 = (0.80)^2 = 0.6400$$</div>
    </div>
    <div class="row">
      <div class="lab">(ค) สัมประสิทธิ์ Cd</div>
      <div>$$C_d = C_v \times C_c = (0.9783) \times (0.6400) = 0.6261$$</div>
    </div>
    <div class="row">
      <div class="lab">คำตอบสุดท้าย</div>
      <div><span class="fin">\(C_v = 0.978,\quad C_c = 0.640,\quad C_d = 0.626\)</span></div>
    </div>
  </div>

  <div class="pn">
    <a href="#lab7">← บทที่ 7 การสูญเสียในท่อ</a>
    <a href="#lab9">บทที่ 9 การทดสอบเครื่องสูบน้ำ →</a>
  </div>
</section>
'''
