# -*- coding: utf-8 -*-

def get_section_lab11():
    return r'''
<section id="lab11">
  <header class="top">
    <p class="kick">ปฏิบัติการที่ 11 · การไหลวิกฤตและการวัดอัตราการไหลในคลองส่งน้ำชลประทาน</p>
    <h1>บทที่ 11: รางน้ำแบบเวนจูรี่ (Venturi Flume)</h1>
    <p class="sub">Free Flow Condition · Critical Depth (yc = 2/3 H) · Submerged Flow Condition · ข้อดีเหนือฝาย</p>
    <p class="by">CE 272 ปฏิบัติการกลศาสตร์ของไหล · ภาควิชาวิศวกรรมโยธา มหาวิทยาลัยธรรมศาสตร์</p>
    <p class="pracnote">โหมดฝึกเปิดอยู่: ซ่อนวิธีทำไว้ แตะแต่ละขั้นเพื่อดู (ลองเขียนเองก่อน) กดปุ่ม "ฝึก" อีกครั้งเพื่อปิด</p>
  </header>

  <h2 class="prob"><span class="tag">บทที่ 11</span>รางเวนจูรี่และการไหลวิกฤตในทางน้ำเปิด</h2>
  <div class="stmt">
    <p>รางน้ำแบบเวนจูรี่ (Venturi Flume) เป็นโครงสร้างชลศาสตร์ที่นิยมสร้างในคลองส่งน้ำชลประทาน เพื่อบีบลดขนาดความกว้างของทางน้ำเปิดลงจนเกิด <b>สภาวะการไหลวิกฤต (Critical Flow)</b> ตรงบริเวณคอคอด ทำให้สามารถคำนวณอัตราการไหลได้โดยการ <b>วัดระดับน้ำต้นน้ำ (\(y_1\)) เพียงจุดเดียว</b> โดยไม่ต้องวัดความเร็ว</p>
  </div>

  <div class="jump">
    <a href="#lab11-advantages">ก. ข้อดีเหนือฝายและการทำงาน</a>
    <a href="#lab11-diagram">ข. แผนภาพรางเวนจูรี่ (Top View &amp; Side View)</a>
    <a href="#lab11-freeflow">ค. การไหลแบบอิสระ vs ท้ายน้ำจม</a>
    <a href="#lab11-traps">ง. จุดดักคะแนนข้อสอบ</a>
    <a href="#lab11-exam">จ. ตัวอย่างโจทย์ข้อสอบและการแสดงวิธีทำ</a>
  </div>

  <h3 class="grp" id="lab11-advantages">ก. ข้อดีของรางเวนจูรี่เมื่อเปรียบเทียบกับฝาย</h3>
  <div class="bx chk">
    <b>จุดเด่นเชิงวิศวกรรมชลศาสตร์ (หน้า 85 ในคู่มือ):</b>
    <div>
      1. <b>การสูญเสียพลังงานน้อยกว่ามาก:</b> เนื่องจากโครงสร้างเป็นแบบลู่เข้าและผายออกอย่างค่อยเป็นค่อยไป (Streamlined) ไม่ใช่สิ่งกีดขวางตั้งฉากแบบฝาย<br>
      2. <b>ไม่มีการตกตะกอนสะสม (Self-Cleaning):</b> ฝายมักมีบริเวณน้ำนิ่งด้านหน้าทำให้ทรายและตะกอนตกทับถมจนสเกลเพี้ยน แต่รางเวนจูรี่น้ำจะไหลต่อเนื่องด้วยความเร็วสูง ตะกอนจึงถูกพัดพาผ่านคอคอดไปได้หมด<br>
      3. <b>วัด \(Q\) ได้ง่ายมาก:</b> ในสภาวะ Free flow วัดความลึกน้ำต้นน้ำจุดเดียวก็คำนวณ \(Q\) ได้ทันที
    </div>
  </div>

  <h3 class="grp" id="lab11-diagram">ข. แผนภาพรางเวนจูรี่มุมมองบนและด้านข้าง</h3>
  <figure>
    <svg viewBox="0 0 680 300" role="img" aria-label="แผนภาพรางเวนจูรี่ทั้งมุมมองจากด้านบนและด้านข้าง">
      <!-- Top View -->
      <g transform="translate(40, 20)">
        <text x="300" y="18" font-size="14" font-weight="700" text-anchor="middle" fill="var(--navy)">มุมมองจากด้านบน (Top View)</text>
        <!-- Flume Walls Top -->
        <path d="M 40 40 H 180 L 260 65 H 340 L 420 40 H 560" fill="none" stroke="var(--ink)" stroke-width="3"/>
        <path d="M 40 140 H 180 L 260 115 H 340 L 420 140 H 560" fill="none" stroke="var(--ink)" stroke-width="3"/>
        <rect x="42" y="42" width="138" height="96" fill="var(--water)" opacity="0.4"/>
        <polygon points="180,40 260,65 340,65 420,40 420,140 340,115 260,115 180,140" fill="var(--water)" opacity="0.6"/>
        <rect x="420" y="42" width="138" height="96" fill="var(--water)" opacity="0.4"/>

        <!-- Labels -->
        <text x="110" y="95" font-size="13" font-weight="600" text-anchor="middle" fill="var(--navy)">ต้นน้ำ B</text>
        <text x="300" y="95" font-size="13" font-weight="700" text-anchor="middle" fill="var(--red)">คอคอด b (Throat)</text>
        <text x="490" y="95" font-size="13" font-weight="600" text-anchor="middle" fill="var(--navy)">ท้ายน้ำ B</text>
        <!-- Converging / Diverging -->
        <text x="210" y="32" font-size="11" fill="var(--gray)">ส่วนลู่เข้า (Converging)</text>
        <text x="390" y="32" font-size="11" fill="var(--gray)">ส่วนผายออก (Diverging)</text>
      </g>

      <!-- Side View: Free Flow -->
      <g transform="translate(40, 160)">
        <text x="300" y="20" font-size="14" font-weight="700" text-anchor="middle" fill="var(--navy)">มุมมองด้านข้าง: สภาวะการไหลแบบอิสระ (Free Flow)</text>
        <!-- Bed -->
        <line x1="40" y1="110" x2="560" y2="110" stroke="var(--ink)" stroke-width="3"/>
        <!-- Water surface falling to yc -->
        <path d="M 40 50 H 180 Q 240 50 300 80 Q 340 100 420 75 H 560 L 560 110 L 40 110 Z" fill="var(--water)" opacity="0.6"/>
        <!-- Depths -->
        <line x1="120" y1="50" x2="120" y2="110" stroke="var(--navy)" stroke-width="2" marker-start="url(#ar)" marker-end="url(#ar)"/>
        <text x="135" y="85" font-size="13" font-weight="700" fill="var(--navy)">y1 (ต้นน้ำ)</text>

        <line x1="300" y1="80" x2="300" y2="110" stroke="var(--red)" stroke-width="2" marker-start="url(#ar)" marker-end="url(#ar)"/>
        <text x="315" y="100" font-size="13" font-weight="700" fill="var(--red)">yc = (2/3)H</text>
        <text x="300" y="65" font-size="12" font-weight="600" text-anchor="middle" fill="var(--red)">Critical Flow (Fr = 1)</text>
      </g>
    </svg>
    <figcaption>รูปที่ 11.1 รูปร่างของรางเวนจูรี่และการลดระดับผิวน้ำสู่สภาวะวิกฤตที่คอคอด</figcaption>
  </figure>

  <h3 class="grp" id="lab11-freeflow">ค. 2 สภาวะการไหล: Free Flow vs Submerged Flow</h3>

  <div class="ty">
    <div class="tyh">กรณีที่ 1: การไหลแบบอิสระ (Free Flow Condition)</div>
    <div class="tyb">
      <p class="gq">ระดับน้ำท้ายน้ำต่ำ น้ำไหลเทผ่านคอคอดอย่างอิสระ เกิดการไหลวิกฤต (\(Fr = 1\))</p>
      <ol class="st">
        <li>ความลึกวิกฤตที่คอคอด (Critical Depth):
          $$y_c = \frac{2}{3}H \approx \frac{2}{3}y_1\tag{11.6}$$
        </li>
        <li>ความเร็ววิกฤต: \(V_c = \sqrt{g y_c}\)</li>
        <li>อัตราการไหลทางทฤษฎี:
          $$Q_{\text{theory}} = V_c A_c = \sqrt{g y_c}(b y_c) = \sqrt{g} b y_c^{1.5} = \left(\frac{2}{3}\right)^{1.5} \sqrt{g} b H^{1.5}\tag{11.7}$$
          $$Q_{\text{theory}} \approx \left(\frac{2}{3}\right)^{1.5} \sqrt{g} b y_1^{1.5}\tag{11.8}$$
        </li>
      </ol>
    </div>
  </div>

  <div class="ty">
    <div class="tyh">กรณีที่ 2: การไหลแบบท้ายน้ำจม (Submerged Flow Condition)</div>
    <div class="tyb">
      <p class="gq">ระดับน้ำท้ายน้ำหนุนสูงท่วมคอคอด ไม่เกิดสภาวะวิกฤต (\(Fr < 1\)) ต้องวัดความลึกน้ำทั้ง 2 จุด (\(y_1\) และ \(y_2\))</p>
      <ol class="st">
        <li>ใช้อนุรักษ์พลังงานระหว่างจุด 1 (ต้นน้ำ) และจุด 2 (คอคอด):
          $$y_1 + \frac{V_1^2}{2g} = y_2 + \frac{V_2^2}{2g}\tag{11.9}$$
        </li>
        <li>อัตราการไหลทางทฤษฎี:
          $$Q_{\text{theory}} = a \sqrt{\frac{2g(y_1 - y_2)}{1 - M^2}}\tag{11.17}$$
          <p class="nt">โดย \(a = b y_2\), \(A = B y_1\) และ \(M = \frac{a}{A} = \frac{b y_2}{B y_1}\)</p>
        </li>
        <li>อัตราการไหลจริง: \(Q_{\text{actual}} = C_d Q_{\text{theory}}\)</li>
      </ol>
    </div>
  </div>

  <h3 class="grp" id="lab11-traps">ง. จุดดักคะแนนข้อสอบ</h3>
  <div class="bx trap">
    <b>ที่มาของตัวเลข 2/3 ในสูตร \(y_c = \frac{2}{3}H\):</b>
    <div>
      สำหรับทางน้ำเปิดรูปสี่เหลี่ยมผืนผ้า พลังงานจำเพาะคือ \(E = y + \frac{q^2}{2gy^2}\)<br>
      • จุดที่มีพลังงานจำเพาะต่ำที่สุด (\(\frac{dE}{dy} = 0\)) จะได้ความลึกวิกฤต \(y_c = \left(\frac{q^2}{g}\right)^{1/3}\)<br>
      • และพลังงานจำเพาะต่ำสุดคือ \(E_{\min} = y_c + \frac{y_c}{2} = \frac{3}{2}y_c\)<br>
      • ดังนั้น \(y_c = \frac{2}{3}E_{\min} = \frac{2}{3}H\) ตัวเลข \(\frac{2}{3}\) นี้จึงเป็นค่าคงที่ทางฟิสิกส์ของการไหลในรางสี่เหลี่ยมผืนผ้า!
    </div>
  </div>

  <h3 class="grp" id="lab11-exam">จ. ตัวอย่างโจทย์ข้อสอบและการแสดงวิธีทำ (Exam Practice)</h3>
  <div class="stmt">
    <p><b>โจทย์ตัวอย่าง:</b> รางเวนจูรี่มีคอคอดกว้าง \(b = 15\text{ cm}\) ทำงานในสภาวะ Free Flow Condition วัดระดับความลึกน้ำต้นน้ำได้ \(y_1 = 20.0\text{ cm}\) จงหา (ก) ความลึกวิกฤตที่คอคอด \(y_c\) (ข) ความเร็วการไหลที่คอคอด \(V_c\) และ (ค) อัตราการไหลทางทฤษฎี \(Q_{\text{th}}\)</p>
  </div>

  <h4 class="cardt">เฉลยวิธีทำ (เขียนส่งอาจารย์ตามลำดับ)</h4>
  <div class="exam">
    <div class="row">
      <div class="lab">ข้อมูลที่กำหนด</div>
      <div class="given">$$\begin{aligned} & b = 0.15\ \text{m},\quad y_1 = 0.200\ \text{m} \\ & \text{สภาวะ Free Flow}\ (Fr = 1) \end{aligned}$$</div>
    </div>
    <div class="row">
      <div class="lab">(ก) ความลึกวิกฤต yc</div>
      <div>$$y_c = \frac{2}{3}y_1 = \frac{2}{3}(0.200\ \text{m}) = 0.1333\ \text{m} = 13.33\ \text{cm}$$</div>
    </div>
    <div class="row">
      <div class="lab">(ข) ความเร็ววิกฤต Vc</div>
      <div>$$V_c = \sqrt{g y_c} = \sqrt{(9.81)(0.1333)} = \sqrt{1.3080} = 1.1437\ \text{m/s}$$</div>
    </div>
    <div class="row">
      <div class="lab">(ค) อัตราการไหล Qth</div>
      <div>$$\begin{aligned} A_c &= b \cdot y_c = (0.15)(0.1333) = 0.0200\ \text{m}^2 \\ Q_{\text{th}} &= V_c A_c = (1.1437)(0.0200) = 0.02287\ \text{m}^3/\text{s} \\ &= 22.87\ \text{L/s} = 82.35\ \text{m}^3/\text{hr} \end{aligned}$$<p class="nt" style="color:var(--green);font-weight:600;margin:6px 0 0;">(ตรงกับสูตรลัด \(Q = (\frac{2}{3})^{1.5} \sqrt{g}\, b\, y_1^{1.5}\))</p></div>
    </div>
    <div class="row">
      <div class="lab">คำตอบสุดท้าย</div>
      <div><span class="fin">\(y_c = 13.3\ \text{cm},\quad V_c = 1.14\ \text{m/s},\quad Q_{\text{th}} = 0.0229\ \text{m}^3/\text{s}\ (22.9\ \text{L/s})\)</span></div>
    </div>
  </div>

  <div class="pn">
    <a href="#lab10">← บทที่ 10 การไหลลอดประตูน้ำ</a>
    <a href="#exam">คลังข้อสอบ &amp; โหมดฝึก →</a>
  </div>
</section>
'''
