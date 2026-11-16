# -*- coding: utf-8 -*-

def get_section_lab3():
    return r'''
<section id="lab3">
  <header class="top">
    <p class="kick">ปฏิบัติการที่ 3 · พลศาสตร์ของไหลและการถ่ายเทพลังงานกล</p>
    <h1>บทที่ 3: แรงกระแทกของลำน้ำ (Impact of Jet)</h1>
    <p class="sub">Impulse-Momentum Principle · การพุ่งชนแผ่นเป้า 90° แบน เทียบกับ ถ้วยครึ่งวงกลม 180°</p>
    <p class="by">CE 272 ปฏิบัติการกลศาสตร์ของไหล · ภาควิชาวิศวกรรมโยธา มหาวิทยาลัยธรรมศาสตร์</p>
    <p class="pracnote">โหมดฝึกเปิดอยู่: ซ่อนวิธีทำไว้ แตะแต่ละขั้นเพื่อดู (ลองเขียนเองก่อน) กดปุ่ม "ฝึก" อีกครั้งเพื่อปิด</p>
  </header>

  <h2 class="prob"><span class="tag">บทที่ 3</span>หลักการอนุรักษ์โมเมนตัมและแรงกระแทกลำน้ำ</h2>
  <div class="stmt">
    <p>การทดลองนี้ศึกษาแรงกระทำที่เกิดจากการถ่ายทอดโมเมนตัมของลำน้ำความเร็วสูงที่พุ่งออกจากหัวฉีด (Nozzle) เข้าชนแผ่นเป้า (Vanes) ที่มีรูปทรงเรขาคณิตต่างกัน ซึ่งเป็นหัวใจสำคัญในการออกแบบกังหันน้ำผลิตไฟฟ้า เช่น กังหันแบบเพลตัน (Pelton Wheel Turbine)</p>
  </div>

  <div class="jump">
    <a href="#lab3-principle">ก. วัตถุประสงค์และหลักการ First Principles</a>
    <a href="#lab3-diagram">ข. อุปกรณ์และการเปรียบเทียบแผ่นเป้า</a>
    <a href="#lab3-eq">ค. สูตรและการวิเคราะห์กราฟความชัน</a>
    <a href="#lab3-traps">ง. จุดดักคะแนนข้อสอบ</a>
    <a href="#lab3-exam">จ. ตัวอย่างโจทย์ข้อสอบและการแสดงวิธีทำ</a>
  </div>

  <h3 class="grp" id="lab3-principle">ก. วัตถุประสงค์และหลักการ First Principles</h3>
  <p>จากกฎการเคลื่อนที่ข้อที่ 2 ของนิวตัน (\(\sum \vec{F} = \frac{d\vec{M}}{dt}\)) แรงที่ฉากกั้นกระทำต่อลำน้ำจะเท่ากับอัตราการเปลี่ยนแปลงโมเมนตัมของลำน้ำ สำหรับการไหลแบบคงตัว (Steady Incompressible Flow) จะได้:</p>
  
  $$\vec{F} = \dot{m}(\vec{v}_{\text{out}} - \vec{v}_{\text{in}}) = \rho Q (\vec{v}_{\text{out}} - \vec{v}_{\text{in}})\tag{3.4}$$

  <p>เมื่อลำน้ำพุ่งขึ้นในแนวดิ่งด้วยความเร็ว \(v\) เข้าชนฉากกั้นที่เบนทิศทางลำน้ำเป็นมุม \(\theta\) กับแนวดิ่ง (กำหนดให้ทิศลงเป็นบวกตามแรงโน้มถ่วง) จะได้แรงต้านในแนวดิ่งคือ:</p>
  
  $$F = \rho Q (v \cos\theta - (-v)) = \rho Q v (\cos\theta + 1) = \rho A v^2 (\cos\theta + 1)\tag{3.5}$$

  <h3 class="grp" id="lab3-diagram">ข. การเปรียบเทียบแผ่นเป้า (Flat Plate vs Hemispherical Cup)</h3>
  <figure>
    <svg viewBox="0 0 680 260" role="img" aria-label="เปรียบเทียบทิศทางลำน้ำระหว่างแผ่นแบนกับถ้วยครึ่งวงกลม">
      <!-- Flat Plate 90 deg -->
      <g transform="translate(60, 20)">
        <text x="120" y="20" font-size="15" font-weight="700" text-anchor="middle" fill="var(--navy)">1. แผ่นเรียบแบน 90° (Flat Plate)</text>
        <line x1="40" y1="60" x2="200" y2="60" stroke="var(--ink)" stroke-width="6"/>
        <!-- Incoming jet -->
        <line x1="120" y1="180" x2="120" y2="65" stroke="var(--blue)" stroke-width="4" marker-end="url(#ar)"/>
        <text x="130" y="140" font-size="13" fill="var(--blue)">v_in = v</text>
        <!-- Outgoing jets -->
        <line x1="120" y1="65" x2="30" y2="65" stroke="var(--blue)" stroke-width="3" marker-end="url(#ar)"/>
        <line x1="120" y1="65" x2="210" y2="65" stroke="var(--blue)" stroke-width="3" marker-end="url(#ar)"/>
        <text x="120" y="95" font-size="12" fill="var(--gray)" text-anchor="middle">น้ำกระจายออกแนวราบ (\(v_{y,\text{out}} = 0\))</text>
        <!-- Formula box -->
        <rect x="35" y="195" width="170" height="35" fill="var(--hover)" stroke="var(--rule)"/>
        <text x="120" y="218" font-size="15" font-weight="700" text-anchor="middle" fill="var(--red)">\(F = \rho Q v\)</text>
      </g>

      <!-- Hemispherical Cup 180 deg -->
      <g transform="translate(380, 20)">
        <text x="120" y="20" font-size="15" font-weight="700" text-anchor="middle" fill="var(--navy)">2. ถ้วยครึ่งวงกลม 180° (Hemispherical)</text>
        <!-- Cup arc -->
        <path d="M 40 100 A 80 80 0 0 1 200 100" fill="none" stroke="var(--ink)" stroke-width="6"/>
        <!-- Incoming jet -->
        <line x1="120" y1="180" x2="120" y2="40" stroke="var(--blue)" stroke-width="4" marker-end="url(#ar)"/>
        <text x="130" y="140" font-size="13" fill="var(--blue)">v_in = v</text>
        <!-- Outgoing reverse jets -->
        <line x1="50" y1="95" x2="50" y2="160" stroke="var(--blue)" stroke-width="3" marker-end="url(#ar)"/>
        <line x1="190" y1="95" x2="190" y2="160" stroke="var(--blue)" stroke-width="3" marker-end="url(#ar)"/>
        <text x="120" y="95" font-size="12" fill="var(--gray)" text-anchor="middle">ลำน้ำเลี้ยวกลับ 180° (\(v_{y,\text{out}} = -v\))</text>
        <!-- Formula box -->
        <rect x="30" y="195" width="180" height="35" fill="var(--hover)" stroke="var(--rule)"/>
        <text x="120" y="218" font-size="15" font-weight="700" text-anchor="middle" fill="var(--red)">\(F = 2\rho Q v\)  (แรงเป็น 2 เท่า!)</text>
      </g>
    </svg>
    <figcaption>รูปที่ 3.1 การเลี้ยวทิศทางของโมเมนตัมลำน้ำบนแผ่นเป้าแบบเรียบและแบบถ้วยครึ่งวงกลม</figcaption>
  </figure>

  <h3 class="grp" id="lab3-eq">ค. สูตรและการวิเคราะห์กราฟความชัน</h3>
  <ol class="st">
    <li><b>แผ่นเรียบแบน (\(\theta = 90^\circ\)):</b>
      $$\cos 90^\circ = 0 \Rightarrow F_{\text{flat}} = \rho Q v = \rho A v^2\tag{3.6}$$
    </li>
    <li><b>ถ้วยครึ่งวงกลม (\(\theta = 0^\circ\)):</b>
      $$\cos 0^\circ = 1 \Rightarrow F_{\text{hemi}} = 2\rho Q v = 2\rho A v^2\tag{3.7}$$
    </li>
    <li><b>ฉากเอียงมุมอื่นๆ:</b>
      - ฉาก \(30^\circ\): \(F = \rho Q v (\cos 30^\circ + 1) = 1.866 \rho Q v\)<br>
      - ฉาก \(120^\circ\): \(F = \rho Q v (\cos 120^\circ + 1) = 0.500 \rho Q v\)
    </li>
  </ol>

  <p><b>การวิเคราะห์ความชันกราฟ (Slope Analysis):</b></p>
  <p>เมื่อเขียนกราฟความสัมพันธ์ระหว่างแรงจากตุ้มน้ำหนัก \(F = mg\) [แกน Y] กับ \(v^2\) [แกน X] จะได้สมการเส้นตรงผ่านจุดกำเนิด:</p>
  $$\text{Slope} = \rho A (\cos\theta + 1)$$
  <p>โดยที่ \(A = \frac{\pi d_0^2}{4}\) คือพื้นที่หน้าตัดหัวฉีด (ขนาด \(d_0 \approx 8\text{ mm}\)) สามารถนำค่า Slope มาคำนวณหามุม \(\theta\) ของฉากกั้นได้อย่างแม่นยำ</p>

  <h3 class="grp" id="lab3-traps">ง. จุดดักคะแนนข้อสอบ</h3>
  <div class="bx trap">
    <b>ทำไมถ้วยครึ่งวงกลมถึงรับแรงกระแทกเป็น 2 เท่าของแผ่นเรียบ?</b>
    <div>
      ข้อสอบบรรยายชอบถามข้อนี้บ่อยมาก!<br>
      • <b>แผ่นแบน:</b> ทำหน้าที่เพียง <i>หยุดความเร็วในแนวดิ่ง</i> (\(v_{\text{in}} = v \to v_{\text{out}} = 0\)) การเปลี่ยนแปลงโมเมนตัมคือ \(\Delta v = 0 - (-v) = v\)<br>
      • <b>ถ้วยครึ่งวงกลม:</b> นอกจากหยุดความเร็วแล้ว ยัง <i>ดันลำน้ำให้สะท้อนกลับทิศทางเดิม</i> (\(v_{\text{in}} = v \to v_{\text{out}} = -v\)) ทำให้การเปลี่ยนแปลงโมเมนตัมรวมคือ \(\Delta v = v - (-v) = 2v\)<br>
      • ดังนั้น แรงกระทำสุทธิจึงเป็น <b>2 เท่า</b> พอดีเสมอ
    </div>
  </div>

  <h3 class="grp" id="lab3-exam">จ. ตัวอย่างโจทย์ข้อสอบและการแสดงวิธีทำ (Exam Practice)</h3>
  <div class="stmt">
    <p><b>โจทย์ตัวอย่าง:</b> หัวฉีดเส้นผ่านศูนย์กลาง \(d_0 = 8\text{ mm}\) ฉีดน้ำด้วยอัตราการไหล \(Q = 0.50\text{ L/s}\) พุ่งชน (ก) แผ่นเรียบแบน 90° และ (ข) ถ้วยครึ่งวงกลม 180° จงหาแรงกระแทก \(F\) ของแต่ละกรณี และหามวลตุ้มน้ำหนัก \(m\) ที่ต้องใช้วางเพื่อรักษาสมดุลของระบบ (\(g = 9.81\text{ m/s}^2, \rho = 1000\text{ kg/m}^3\))</p>
  </div>

  <h4 class="cardt">เฉลยวิธีทำ (เขียนส่งอาจารย์ตามลำดับ)</h4>
  <div class="exam">
    <div class="row">
      <div class="lab">ข้อมูลที่กำหนด</div>
      <div class="given">$$\begin{aligned} & d_0 = 8\ \text{mm} = 0.008\ \text{m} \\ & Q = 0.50\ \text{L/s} = 0.50 \times 10^{-3}\ \text{m}^3/\text{s} \\ & \rho = 1000\ \text{kg/m}^3,\quad g = 9.81\ \text{m/s}^2 \end{aligned}$$</div>
    </div>
    <div class="row">
      <div class="lab">พื้นที่และ v</div>
      <div>$$\begin{aligned} A &= \frac{\pi(0.008)^2}{4} = 5.0265 \times 10^{-5}\ \text{m}^2 \\ v &= \frac{Q}{A} = \frac{0.50 \times 10^{-3}}{5.0265 \times 10^{-5}} = 9.947\ \text{m/s} \end{aligned}$$</div>
    </div>
    <div class="row">
      <div class="lab">(ก) แผ่นแบน 90°</div>
      <div>$$\begin{aligned} F_{\text{flat}} &= \rho Q v = (1000)(0.50 \times 10^{-3})(9.947) = 4.974\ \text{N} \\ m_{\text{flat}} &= \frac{F}{g} = \frac{4.974}{9.81} = 0.5070\ \text{kg} = 507.0\ \text{g} \end{aligned}$$</div>
    </div>
    <div class="row">
      <div class="lab">(ข) ถ้วยครึ่งวงกลม 180°</div>
      <div>$$\begin{aligned} F_{\text{hemi}} &= 2\rho Q v = 2 \times 4.974 = 9.947\ \text{N}\quad (\text{เป็น 2 เท่า}) \\ m_{\text{hemi}} &= \frac{9.947}{9.81} = 1.0140\ \text{kg} = 1014.0\ \text{g} \end{aligned}$$</div>
    </div>
    <div class="row">
      <div class="lab">คำตอบสุดท้าย</div>
      <div><span class="fin">แผ่นแบน: \(F = 4.97\ \text{N}\ (m = 507\ \text{g})\) · ถ้วยครึ่งวงกลม: \(F = 9.95\ \text{N}\ (m = 1014\ \text{g})\)</span></div>
    </div>
  </div>

  <div class="pn">
    <a href="#lab2">← บทที่ 2 จุดศูนย์กลางแรงดัน</a>
    <a href="#lab4">บทที่ 4 สมการเบอร์นูลี่ →</a>
  </div>
</section>
'''
