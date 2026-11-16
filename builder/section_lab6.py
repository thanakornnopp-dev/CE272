# -*- coding: utf-8 -*-

def get_section_lab6():
    return r'''
<section id="lab6">
  <header class="top">
    <p class="kick">ปฏิบัติการที่ 6 · การวัดอัตราการไหลในทางน้ำเปิดด้วยสิ่งกีดขวาง</p>
    <h1>บทที่ 6: การวัดอัตราการไหลด้วยฝาย (Flow over Weir)</h1>
    <p class="sub">ฝายสันคมสี่เหลี่ยมผืนผ้า (H^1.5) · ฝายสามเหลี่ยมตัววี 90° (H^2.5) · Hook Gauge · การหาค่า Cd</p>
    <p class="by">CE 272 ปฏิบัติการกลศาสตร์ของไหล · ภาควิชาวิศวกรรมโยธา มหาวิทยาลัยธรรมศาสตร์</p>
    <p class="pracnote">โหมดฝึกเปิดอยู่: ซ่อนวิธีทำไว้ แตะแต่ละขั้นเพื่อดู (ลองเขียนเองก่อน) กดปุ่ม "ฝึก" อีกครั้งเพื่อปิด</p>
  </header>

  <h2 class="prob"><span class="tag">บทที่ 6</span>การไหลข้ามฝายและการวิเคราะห์สัมประสิทธิ์การไหล</h2>
  <div class="stmt">
    <p>ฝาย (Weir) คือสิ่งกีดขวางที่สร้างขวางทางน้ำเปิดเพื่อให้น้ำไหลล้นข้ามสันฝาย โดยอาศัยความสัมพันธ์ระหว่าง <b>ความสูงของระดับน้ำเหนือสันฝาย (\(H\))</b> กับ <b>อัตราการไหล (\(Q\))</b> การทดลองนี้ศึกษาฝาย 2 ชนิดหลักที่นิยมใช้ในงานวิศวกรรมชลศาสตร์ คือ ฝายสันคมสี่เหลี่ยม (Rectangular Weir) และฝายสามเหลี่ยมตัววี 90° (V-Notch Weir)</p>
  </div>

  <div class="jump">
    <a href="#lab6-theory">ก. วัตถุประสงค์และการพิสูจน์สูตร</a>
    <a href="#lab6-diagram">ข. อุปกรณ์และ Hook Gauge</a>
    <a href="#lab6-comparison">ค. เปรียบเทียบฝายสี่เหลี่ยม vs ฝายสามเหลี่ยม</a>
    <a href="#lab6-traps">ง. จุดดักคะแนนข้อสอบ</a>
    <a href="#lab6-exam">จ. ตัวอย่างโจทย์ข้อสอบและการแสดงวิธีทำ</a>
  </div>

  <h3 class="grp" id="lab6-theory">ก. วัตถุประสงค์และการพิสูจน์สูตร (Derivation of Weir Formulas)</h3>
  <p>พิจารณาชิ้นส่วนการไหลเล็กๆ ที่ระดับความลึก \(h\) จากผิวน้ำ มีความกว้าง \(b\) และความหนา \(dh\) ความเร็วตามกฎของทอร์ริเชลลีคือ \(v = \sqrt{2gh}\) อัตราการไหลย่อยคือ \(dQ = b \sqrt{2gh} \, dh\) เมื่ออินทิเกรตตลอดความสูงช่องเปิด \(H\):</p>
  
  $$Q = \int_0^H b \sqrt{2gh} \, dh\tag{6.3}$$

  <div class="ty">
    <div class="tyh">1. ฝายรูปสี่เหลี่ยมผืนผ้า (Rectangular Weir: ความกว้าง \(B\) คงที่)</div>
    <div class="tyb">
      <p>เนื่องจากความกว้าง \(b = B\) คงที่ตลอดความลึก ดึงออกมานอกเครื่องหมายอินทิเกรต:</p>
      $$Q_{\text{theory}} = B \sqrt{2g} \int_0^H h^{1/2} \, dh = \frac{2}{3} B \sqrt{2g} H^{3/2}\tag{6.4}$$
      $$Q_{\text{actual}} = C_d \frac{2}{3} B \sqrt{2g} H^{3/2}\tag{6.5}$$
      <p class="gq">• ความสัมพันธ์: \(Q \propto H^{1.5}\) (กำลัง 1.5)</p>
    </div>
  </div>

  <div class="ty">
    <div class="tyh">2. ฝายรูปสามเหลี่ยมตัววี (V-Notch Weir: มุมรวม \(\theta\))</div>
    <div class="tyb">
      <p>ความกว้างช่องเปิดจะแปรผันตามความลึก: \(b = 2(H - h)\tan\left(\frac{\theta}{2}\right)\) แทนค่าแล้วอินทิเกรต:</p>
      $$Q_{\text{theory}} = \frac{8}{15} \sqrt{2g} \tan\left(\frac{\theta}{2}\right) H^{5/2}\tag{6.7}$$
      <p>สำหรับฝายสามเหลี่ยมมุมฉากในห้องแล็บ (\(\theta = 90^\circ \Rightarrow \tan 45^\circ = 1\)):</p>
      $$Q_{\text{theory}} = \frac{8}{15} \sqrt{2g} H^{5/2} \approx 2.361 H^{2.5}$$
      $$Q_{\text{actual}} = C_d \frac{8}{15} \sqrt{2g} H^{5/2}\tag{6.8}$$
      <p class="gq">• ความสัมพันธ์: \(Q \propto H^{2.5}\) (กำลัง 2.5)</p>
    </div>
  </div>

  <h3 class="grp" id="lab6-diagram">ข. อุปกรณ์และการตั้งศูนย์ Hook Gauge</h3>
  <figure>
    <svg viewBox="0 0 680 260" role="img" aria-label="ภาพเปรียบเทียบรูปทรงฝายสี่เหลี่ยมและฝายสามเหลี่ยมพร้อมระดับ H">
      <!-- Rectangular Weir -->
      <g transform="translate(60, 20)">
        <text x="120" y="20" font-size="15" font-weight="700" text-anchor="middle" fill="var(--navy)">ฝายสี่เหลี่ยม (Rectangular)</text>
        <rect x="30" y="45" width="180" height="150" fill="var(--hover)" stroke="var(--ink)" stroke-width="2"/>
        <!-- Notch cut -->
        <rect x="65" y="45" width="110" height="80" fill="var(--water)" stroke="var(--ink)" stroke-width="2"/>
        <text x="120" y="110" font-size="14" font-weight="600" text-anchor="middle" fill="var(--blue)">น้ำล้นข้ามฝาย</text>
        <!-- Dimension B -->
        <line x1="65" y1="135" x2="175" y2="135" stroke="var(--red)" stroke-width="2" marker-start="url(#ar)" marker-end="url(#ar)"/>
        <text x="120" y="152" font-size="13" font-weight="700" text-anchor="middle" fill="var(--red)">ความกว้าง B</text>
        <!-- Dimension H -->
        <line x1="190" y1="45" x2="190" y2="125" stroke="var(--navy)" stroke-width="1.5" marker-start="url(#ar)" marker-end="url(#ar)"/>
        <text x="200" y="90" font-size="13" font-weight="600" fill="var(--navy)">H</text>
      </g>

      <!-- V-Notch Weir -->
      <g transform="translate(380, 20)">
        <text x="120" y="20" font-size="15" font-weight="700" text-anchor="middle" fill="var(--navy)">ฝายสามเหลี่ยม 90° (V-Notch)</text>
        <rect x="30" y="45" width="180" height="150" fill="var(--hover)" stroke="var(--ink)" stroke-width="2"/>
        <!-- V-cut -->
        <polygon points="40,45 200,45 120,135" fill="var(--water)" stroke="var(--ink)" stroke-width="2"/>
        <text x="120" y="85" font-size="13" font-weight="600" text-anchor="middle" fill="var(--blue)">น้ำล้นข้าม</text>
        <text x="120" y="125" font-size="13" font-weight="700" text-anchor="middle" fill="var(--red)">θ = 90°</text>
        <!-- Dimension H -->
        <line x1="210" y1="45" x2="210" y2="135" stroke="var(--navy)" stroke-width="1.5" marker-start="url(#ar)" marker-end="url(#ar)"/>
        <text x="220" y="95" font-size="13" font-weight="600" fill="var(--navy)">H</text>
      </g>
    </svg>
    <figcaption>รูปที่ 6.1 รูปทรงช่องเปิดของฝายสี่เหลี่ยมผืนผ้าและฝายสามเหลี่ยมมุมฉาก</figcaption>
  </figure>

  <h3 class="grp" id="lab6-comparison">ค. ทำไมฝายสามเหลี่ยมถึงแม่นยำกว่าเมื่อน้ำไหลน้อย?</h3>
  <div class="tw">
    <table>
      <caption>การเปรียบเทียบคุณสมบัติเชิงวิศวกรรมของฝายทั้งสองชนิด</caption>
      <thead>
        <tr><th>คุณลักษณะ</th><th>ฝายสี่เหลี่ยม (Rectangular)</th><th>ฝายสามเหลี่ยม (V-Notch)</th></tr>
      </thead>
      <tbody>
        <tr><td>ความสัมพันธ์ของอัตราการไหล</td><td>\(Q \propto H^{1.5}\)</td><td>\(Q \propto H^{2.5}\)</td></tr>
        <tr><td>ความเหมาะสมในการใช้งาน</td><td>เหมาะกับ <b>อัตราการไหลมาก ๆ (\(Q\) สูง)</b></td><td>เหมาะกับ <b>อัตราการไหลน้อย ๆ (\(Q\) ต่ำ)</b></td></tr>
        <tr><td>ความไวต่อการยกตัวของน้ำ (\(dH/dQ\))</td><td>ที่ \(Q\) ต่ำ น้ำจะล้นแผ่นบางมาก วัด \(H\) ยาก</td><td>ที่ \(Q\) ต่ำ ระดับน้ำ \(H\) จะยกตัวสูงกว่าชัดเจน</td></tr>
        <tr><td>ความคลาดเคลื่อนในการวัด</td><td>ความคลาดเคลื่อนสูงเมื่อน้ำไหลเอื่อย</td><td><b>แม่นยำสูงมาก</b> ในช่วงอัตราการไหลต่ำ</td></tr>
      </tbody>
    </table>
  </div>

  <h3 class="grp" id="lab6-traps">ง. จุดดักคะแนนข้อสอบและข้อควรระวัง</h3>
  <div class="bx trap">
    <b>การตั้งศูนย์ของ Hook Gauge (Zero Setting Trap):</b>
    <div>
      • ก่อนเริ่มทำการทดลอง <b>ต้องปรับปลายแหลมของ Hook Gauge ให้แตะที่ระดับ "สันฝาย (Crest)" พอดี</b> แล้วเซ็ตค่าสเกลเวอร์เนียร์เป็นศูนย์ (หรือจดค่าระดับอ้างอิงเริ่มต้น)<br>
      • ห้ามเซ็ตศูนย์ที่ก้นคลองเด็ดขาด เพราะค่า \(H\) คือ <b>ความสูงของผิวน้ำที่อยู่เหนือสันฝาย</b> เท่านั้น
    </div>
  </div>

  <div class="bx chk">
    <b>การหาค่า \(C_d\) จากกราฟ:</b>
    <div>
      • ฝายสี่เหลี่ยม: พล็อตกราฟแกน \(Y = Q_{\text{act}}\) กับแกน \(X = H^{1.5}\) จะได้ \(\text{Slope} = \frac{2}{3} C_d B \sqrt{2g}\)<br>
      • ฝายสามเหลี่ยม: พล็อตกราฟแกน \(Y = Q_{\text{act}}\) กับแกน \(X = H^{2.5}\) จะได้ \(\text{Slope} = \frac{8}{15} C_d \sqrt{2g}\)<br>
      • หรือใช้กราฟ Log-Log: \(\log Q_{\text{act}} = \log(\text{Constant} \cdot C_d) + m \log H\) โดยความชัน \(m\) จะต้องได้ประมาณ \(1.5\) และ \(2.5\) ตามทฤษฎี
    </div>
  </div>

  <h3 class="grp" id="lab6-exam">จ. ตัวอย่างโจทย์ข้อสอบและการแสดงวิธีทำ (Exam Practice)</h3>
  <div class="stmt">
    <p><b>โจทย์ตัวอย่าง:</b> ในการทดสอบการไหลข้ามฝายสามเหลี่ยมตัววี 90° (\(\theta = 90^\circ\)) วัดระดับน้ำเหนือสันฝายได้ \(H = 65\text{ mm}\) ตวงน้ำได้ปริมาตร \(15\text{ L}\) ในเวลา \(18.2\text{ s}\) จงหา (ก) อัตราการไหลจริง \(Q_{\text{act}}\) (ข) อัตราการไหลทางทฤษฎี \(Q_{\text{th}}\) และ (ค) สัมประสิทธิ์การปรับแก้ \(C_d\)</p>
  </div>

  <h4 class="cardt">เฉลยวิธีทำ (เขียนส่งอาจารย์ตามลำดับ)</h4>
  <div class="exam">
    <div class="row">
      <div class="lab">ข้อมูลที่กำหนด</div>
      <div class="given">$$\begin{aligned} & \theta = 90^\circ \Rightarrow \tan(\theta/2) = \tan 45^\circ = 1.0 \\ & H = 65\ \text{mm} = 0.065\ \text{m} \\ & V = 15\ \text{L} = 0.015\ \text{m}^3,\quad t = 18.2\ \text{s} \end{aligned}$$</div>
    </div>
    <div class="row">
      <div class="lab">(ก) อัตราการไหลจริง</div>
      <div>$$Q_{\text{act}} = \frac{\Delta V}{\Delta t} = \frac{0.015\ \text{m}^3}{18.2\ \text{s}} = 8.2418 \times 10^{-4}\ \text{m}^3/\text{s} = 0.824\ \text{L/s}$$</div>
    </div>
    <div class="row">
      <div class="lab">(ข) อัตราการไหลทฤษฎี</div>
      <div>$$\begin{aligned} Q_{\text{th}} &= \frac{8}{15}\sqrt{2g} \tan(45^\circ) H^{5/2} \\ &= \frac{8}{15}\sqrt{2(9.81)}(1.0)(0.065)^{2.5} \\ &= (2.3619) \times (0.065)^{2.5} = (2.3619)(5.834 \times 10^{-4}) \\ &= 1.378 \times 10^{-3}\ \text{m}^3/\text{s} \end{aligned}$$</div>
    </div>
    <div class="row">
      <div class="lab">(ค) สัมประสิทธิ์ Cd</div>
      <div>$$C_d = \frac{Q_{\text{act}}}{Q_{\text{th}}} = \frac{8.2418 \times 10^{-4}}{1.378 \times 10^{-3}} = 0.5981\quad \htmlClass{ok}{(\text{ช่วงปกติของฝายสันคมคือ 0.58-0.62})}$$</div>
    </div>
    <div class="row">
      <div class="lab">คำตอบสุดท้าย</div>
      <div><span class="fin">\(Q_{\text{act}} = 8.24 \times 10^{-4}\ \text{m}^3/\text{s},\quad Q_{\text{th}} = 1.38 \times 10^{-3}\ \text{m}^3/\text{s},\quad C_d = 0.598\)</span></div>
    </div>
  </div>

  <div class="pn">
    <a href="#lab5">← บทที่ 5 สมการแมนนิ่ง</a>
    <a href="#lab7">บทที่ 7 การสูญเสียพลังงานในท่อ →</a>
  </div>
</section>
'''
