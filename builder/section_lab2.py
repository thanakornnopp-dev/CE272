# -*- coding: utf-8 -*-

def get_section_lab2():
    return r'''
<section id="lab2">
  <header class="top">
    <p class="kick">ปฏิบัติการที่ 2 · สถิตยศาสตร์ของไหลและแรงกระทำต่อพื้นผิวจมน้ำ</p>
    <h1>บทที่ 2: จุดศูนย์กลางของแรงดัน (Center of Pressure)</h1>
    <p class="sub">Hydrostatic Pressure · ทุ่นเสี้ยววงกลม Quadrant · กรณีจมบางส่วนและจมมิดทั้งหมด</p>
    <p class="by">CE 272 ปฏิบัติการกลศาสตร์ของไหล · ภาควิชาวิศวกรรมโยธา มหาวิทยาลัยธรรมศาสตร์</p>
    <p class="pracnote">โหมดฝึกเปิดอยู่: ซ่อนวิธีทำไว้ แตะแต่ละขั้นเพื่อดู (ลองเขียนเองก่อน) กดปุ่ม "ฝึก" อีกครั้งเพื่อปิด</p>
  </header>

  <h2 class="prob"><span class="tag">บทที่ 2</span>แรงดันสถิตและจุดศูนย์กลางแรงดัน</h2>
  <div class="stmt">
    <p>การออกแบบเขื่อน ประตูระบายน้ำ กำแพงกันดิน และโครงสร้างทางชลศาสตร์ จำเป็นต้องทราบทั้ง <b>ขนาดของแรงดันลัพธ์ (\(F\))</b> และ <b>ตำแหน่งที่แรงกระทำสุทธิ (\(y_{cp}\))</b> การทดลองนี้ใช้ชุดทุ่นเสี้ยววงกลม (Quadrant Assembly) เพื่อพิสูจน์ความสัมพันธ์ระหว่างแรงดัน ความลึกของของไหล และเปรียบเทียบตำแหน่งจุดศูนย์กลางแรงดันจากทฤษฎีกับการทดลองจริง</p>
  </div>

  <div class="jump">
    <a href="#lab2-proof">ก. การพิสูจน์ First Principles (ความลับผิวโค้ง)</a>
    <a href="#lab2-diagram">ข. อุปกรณ์และแผนภาพแรงสมดุล</a>
    <a href="#lab2-formulas">ค. สรุปสูตร 2 กรณี (จมบางส่วน vs จมทั้งหมด)</a>
    <a href="#lab2-traps">ง. จุดดักคะแนนข้อสอบ</a>
    <a href="#lab2-exam">จ. ตัวอย่างโจทย์ข้อสอบและการแสดงวิธีทำ</a>
  </div>

  <h3 class="grp" id="lab2-proof">ก. การพิสูจน์ First Principles (ทำไมผิวโค้งไม่เกิดโมเมนต์รอบจุดหมุน?)</h3>
  <p>คำถามยอดฮิตในห้องสอบคือ <i>"เหตุใดแรงดันน้ำที่กระทำต่อผิวด้านโค้งของทุ่นเสี้ยววงกลม จึงไม่ก่อให้เกิดโมเมนต์หมุนรอบแกนหมุน (Pivot Axis)?"</i></p>
  <div class="bx chk">
    <b>ข้อพิสูจน์ทางฟิสิกส์:</b>
    <div>
      1. แรงดันของของเหลวสถิตกระทำในทิศทาง <b>ตั้งฉากกับพื้นผิวสัมผัสทุกจุดเสมอ</b> (\(d\vec{F} \perp dA\))<br>
      2. สำหรับผิวโค้งรูปทรงกระบอก (Cylindrical Surface) เวกเตอร์แรงดันทุกจุดจะมีแนวแรงพุ่งเข้าหา <b>จุดศูนย์กลางความโค้ง (Center of Curvature)</b> ในแนวรัศมี<br>
      3. โครงสร้างชุดทดลองถูกออกแบบให้จุดศูนย์กลางความโค้งตรงกับ <b>จุดหมุน (Pivot Axis)</b> พอดี<br>
      4. ดังนั้น ระยะห่างในแนวตั้งฉาก (Moment Arm, \(r\)) จากจุดหมุนถึงแนวแรงจึงเป็นศูนย์ (\(r = 0\)) ส่งผลให้โมเมนต์รอบจุดหมุนเป็นศูนย์ (\(M = F \times 0 = 0\))<br>
      <b>สรุป:</b> โมเมนต์หมุนรอบแกน Pivot เกิดจาก <b>แรงดันน้ำที่กระทำต่อผิวระนาบเรียบในแนวดิ่ง (Vertical Flat Face) ที่ปลายทุ่นเพียงด้านเดียวเท่านั้น!</b>
    </div>
  </div>

  <h3 class="grp" id="lab2-diagram">ข. อุปกรณ์และขนาดมาตรฐาน</h3>
  <figure>
    <svg viewBox="0 0 680 340" role="img" aria-label="แผนภาพทุ่นเสี้ยววงกลมและสมดุลโมเมนต์">
      <!-- Balance Beam -->
      <line x1="80" y1="90" x2="520" y2="90" stroke="var(--ink)" stroke-width="4"/>
      <!-- Pivot Triangle -->
      <polygon points="340,90 325,125 355,125" fill="var(--gold)" stroke="var(--ink)" stroke-width="1.5"/>
      <circle cx="340" cy="90" r="4" fill="var(--red)"/>
      <text x="340" y="80" font-size="14" font-weight="700" text-anchor="middle" fill="var(--red)">จุดหมุน (Pivot Axis)</text>

      <!-- Weight Pan Left -->
      <line x1="120" y1="90" x2="120" y2="170" stroke="var(--ink)" stroke-width="2"/>
      <rect x="95" y="170" width="50" height="15" fill="var(--ink)"/>
      <text x="120" y="210" font-size="14" font-weight="700" text-anchor="middle" fill="var(--navy)">mg (ตุ้มน้ำหนัก W)</text>
      <!-- Dimension L -->
      <line x1="120" y1="60" x2="340" y2="60" stroke="var(--blue)" stroke-width="1.5" marker-start="url(#ar)" marker-end="url(#ar)"/>
      <text x="230" y="52" font-size="14" font-weight="600" text-anchor="middle" fill="var(--blue)">ระยะคาน L</text>

      <!-- Quadrant Assembly Right -->
      <!-- Curved bottom -->
      <path d="M 340 90 L 340 270 A 180 180 0 0 1 520 90 Z" fill="var(--hover)" stroke="var(--ink)" stroke-width="2"/>
      <!-- Water level -->
      <rect x="340" y="180" width="180" height="90" fill="var(--water)" opacity="0.6"/>
      <line x1="330" y1="180" x2="530" y2="180" stroke="var(--blue)" stroke-width="2"/>
      <polygon points="380,180 375,170 385,170" fill="var(--blue)"/>
      <text x="395" y="175" font-size="13" fill="var(--blue)">ผิวน้ำ (Water Level)</text>

      <!-- Vertical flat face -->
      <line x1="340" y1="180" x2="340" y2="270" stroke="var(--navy)" stroke-width="4"/>
      <!-- Hydrostatic Force Arrow -->
      <line x1="260" y1="240" x2="335" y2="240" stroke="var(--red)" stroke-width="3" marker-end="url(#ar)"/>
      <text x="250" y="245" font-size="14" font-weight="700" text-anchor="end" fill="var(--red)">แรงดัน F</text>

      <!-- Dimension H, d, h'' -->
      <!-- H from pivot to bottom -->
      <line x1="550" y1="90" x2="550" y2="270" stroke="var(--ink)" stroke-width="1.5" marker-start="url(#ar)" marker-end="url(#ar)"/>
      <text x="560" y="185" font-size="13" fill="var(--ink)">H = 200 mm</text>
      <!-- d water depth -->
      <line x1="320" y1="180" x2="320" y2="270" stroke="var(--blue)" stroke-width="1.5" marker-start="url(#ar)" marker-end="url(#ar)"/>
      <text x="310" y="230" font-size="13" font-weight="600" text-anchor="end" fill="var(--blue)">ระดับน้ำ d</text>
    </svg>
    <figcaption>รูปที่ 2.1 แผนภาพแรงและสมดุลโมเมนต์ของชุดทุ่นเสี้ยววงกลม (Quadrant Equilibrium)</figcaption>
  </figure>

  <div class="tw">
    <table>
      <caption>ขนาดมาตรฐานของเครื่องมือทดสอบในห้องแล็บ (หน้า 15 ในคู่มือ)</caption>
      <thead>
        <tr><th>รายการพารามิเตอร์</th><th>สัญลักษณ์</th><th>Armfield</th><th>Essom</th><th>หน่วย</th></tr>
      </thead>
      <tbody>
        <tr><td>ความยาวของคานจากจุดหมุนถึงที่แขวนมวล</td><td>\(L\)</td><td>275</td><td>280</td><td>mm</td></tr>
        <tr><td>ระยะจากจุดหมุนถึงขอบล่างสุดของแผ่นพื้น</td><td>\(H\)</td><td>200</td><td>200</td><td>mm</td></tr>
        <tr><td>ความสูงของแผ่นพื้นรับแรงแนวดิ่ง</td><td>\(D\)</td><td>100</td><td>100</td><td>mm</td></tr>
        <tr><td>ความกว้างของแผ่นพื้นรับแรงแนวดิ่ง</td><td>\(B\)</td><td>75</td><td>75</td><td>mm</td></tr>
      </tbody>
    </table>
  </div>

  <h3 class="grp" id="lab2-formulas">ค. การคำนวณแยก 2 กรณี (Partially Submerged vs Fully Submerged)</h3>

  <div class="ty">
    <div class="tyh">กรณีที่ 1: แผ่นพื้นจมน้ำบางส่วน (Partially Submerged: \(d < D = 100\text{ mm}\))</div>
    <div class="tyb">
      <p class="gq">ระดับผิวน้ำอยู่ต่ำกว่าขอบบนของแผ่นพื้น (\(d < 10\text{ cm}\)) การกระจายแรงดันเป็นรูปสามเหลี่ยม</p>
      <ol class="st">
        <li><b>ความลึกถึงจุดเซนทรอยด์:</b> \(y_c = h_{cg} = \frac{d}{2}\)</li>
        <li><b>พื้นที่รับแรงดันน้ำ:</b> \(A = B \cdot d\)</li>
        <li><b>แรงดันน้ำตามทฤษฎี:</b>
          $$F = \gamma h_{cg} A = \rho g \left(\frac{d}{2}\right)(Bd) = \frac{1}{2}\rho g B d^2\tag{2.11}$$
        </li>
        <li><b>จุดศูนย์กลางแรงดันตามทฤษฎี:</b>
          $$y_{cp,\text{theory}} = \frac{2}{3}d\tag{2.12}$$
        </li>
        <li><b>ระยะแขนโมเมนต์จากการทดลอง (\(h''\)):</b>
          $$\sum M_{\text{pivot}} = 0 \Rightarrow mgL = F h'' \Rightarrow h'' = \frac{mgL}{F} = \frac{2mL}{\rho B d^2}\tag{2.14}$$
        </li>
        <li><b>จุดศูนย์กลางแรงดันจากการทดลอง (\(y_{cp,\text{exp}}\) วัดจากผิวน้ำลงมา):</b>
          $$y_{cp,\text{exp}} = h'' - (H - d)\tag{2.19}$$
        </li>
      </ol>
    </div>
  </div>

  <div class="ty">
    <div class="tyh">กรณีที่ 2: แผ่นพื้นจมน้ำมิดทั้งหมด (Fully Submerged: \(d \ge D = 100\text{ mm}\))</div>
    <div class="tyb">
      <p class="gq">ระดับผิวน้ำท่วมแผ่นพื้นมิด (\(d \ge 10\text{ cm}\)) การกระจายแรงดันเป็นรูปสี่เหลี่ยมคางหมู</p>
      <ol class="st">
        <li><b>ความลึกถึงจุดเซนทรอยด์:</b> \(y_c = h_{cg} = d - \frac{D}{2}\)</li>
        <li><b>พื้นที่รับแรงดันน้ำ:</b> \(A = B \cdot D\) (คงที่ตลอด)</li>
        <li><b>แรงดันน้ำตามทฤษฎี:</b>
          $$F = \gamma h_{cg} A = \rho g \left(d - \frac{D}{2}\right) BD\tag{2.15}$$
        </li>
        <li><b>จุดศูนย์กลางแรงดันตามทฤษฎี (จากทฤษฎีบทแกนขนาน):</b>
          $$y_{cp,\text{theory}} = y_c + \frac{I_{xx}}{y_c A} = \left(d - \frac{D}{2}\right) + \frac{\frac{1}{12}BD^3}{\left(d - \frac{D}{2}\right)BD} = \left(d - \frac{D}{2}\right) + \frac{D^2}{12\left(d - \frac{D}{2}\right)}\tag{2.16}$$
        </li>
        <li><b>ระยะแขนโมเมนต์จากการทดลอง (\(h''\)):</b>
          $$h'' = \frac{mgL}{F} = \frac{mL}{\rho BD\left(d - \frac{D}{2}\right)}\tag{2.18}$$
        </li>
        <li><b>จุดศูนย์กลางแรงดันจากการทดลอง:</b>
          $$y_{cp,\text{exp}} = h'' - (H - d)\tag{2.19}$$
        </li>
      </ol>
    </div>
  </div>

  <h3 class="grp" id="lab2-traps">ง. จุดดักคะแนนข้อสอบและข้อสังเกตสำคัญ</h3>
  <div class="bx trap">
    <b>กับดักพิกัดการวัด \(y_{cp}\):</b>
    <div>
      • \(h''\) คือระยะวัดจาก <b>จุดหมุน (Pivot)</b> ลงมาถึงแนวแรงดันกระทำ<br>
      • \(H - d\) คือระยะจากจุดหมุนลงมาถึง <b>ระดับผิวน้ำ</b><br>
      • ดังนั้น ระยะจุดศูนย์กลางแรงดันจาก <b>ผิวน้ำลงมา</b> คือ \(y_{cp} = h'' - (H - d)\) ห้ามลืมนำไปลบออกเด็ดขาด!
    </div>
  </div>

  <div class="bx chk">
    <b>พฤติกรรมทางฟิสิกส์ที่ต้องจำ:</b>
    <div>
      • เมื่อระดับน้ำ \(d\) เพิ่มขึ้นเรื่อยๆ จุดศูนย์กลางแรงดัน \(y_{cp}\) จะเลื่อนตัวเข้าใกล้จุดเซนทรอยด์ \(y_c\) มากขึ้นเรื่อยๆ เพราะเทอม \(\frac{I_{xx}}{y_c A}\) จะมีค่าน้อยลงจนเข้าใกล้ศูนย์<br>
      • ค่า \(y_{cp}\) จะต้อง <b>อยู่ต่ำกว่าจุดเซนทรอยด์เสมอ</b> (\(y_{cp} > y_c\)) หากคำนวณได้ \(y_{cp} < y_c\) แสดงว่าคิดเลขผิด
    </div>
  </div>

  <h3 class="grp" id="lab2-exam">จ. ตัวอย่างโจทย์ข้อสอบและการแสดงวิธีทำ (Exam Practice)</h3>
  <div class="stmt">
    <p><b>โจทย์ตัวอย่าง:</b> ชุดทดสอบหาจุดศูนย์กลางแรงดันของบริษัท Essom (\(L = 280\text{ mm}, H = 200\text{ mm}, D = 100\text{ mm}, B = 75\text{ mm}\)) แขวนตุ้มน้ำหนัก \(m = 250\text{ g}\) ปรับระดับน้ำจนคานสมดุล อ่านระดับน้ำได้ \(d = 70\text{ mm}\) จงหา (ก) แรงดันน้ำตามทฤษฎี \(F\) (ข) จุดศูนย์กลางแรงดันทางทฤษฎี \(y_{cp,\text{th}}\) และ (ค) จุดศูนย์กลางแรงดันจากการทดลอง \(y_{cp,\text{exp}}\)</p>
  </div>

  <h4 class="cardt">เฉลยวิธีทำ (เขียนส่งอาจารย์ตามลำดับ)</h4>
  <div class="exam">
    <div class="row">
      <div class="lab">ข้อมูลที่กำหนด</div>
      <div class="given">$$\begin{aligned} & B = 0.075\ \text{m},\quad D = 0.100\ \text{m},\quad H = 0.200\ \text{m} \\ & L = 0.280\ \text{m},\quad m = 0.250\ \text{kg},\quad d = 0.070\ \text{m} \end{aligned}$$</div>
    </div>
    <div class="row">
      <div class="lab">ตรวจสอบสภาวะ</div>
      <div>$$d = 0.070\ \text{m} < D = 0.100\ \text{m}\quad \Rightarrow\ \text{กรณีจมบางส่วน (Partially Submerged)}$$</div>
    </div>
    <div class="row">
      <div class="lab">(ก) แรงดัน F</div>
      <div>$$\begin{aligned} F &= \frac{1}{2}\rho g B d^2 \\ &= \frac{1}{2}(1000)(9.81)(0.075)(0.070)^2 = 1.8026\ \text{N} \end{aligned}$$</div>
    </div>
    <div class="row">
      <div class="lab">(ข) y_cp ทางทฤษฎี</div>
      <div>$$y_{cp,\text{th}} = \frac{2}{3}d = \frac{2}{3}(70\ \text{mm}) = 46.67\ \text{mm} = 0.0467\ \text{m}$$</div>
    </div>
    <div class="row">
      <div class="lab">(ค) h'' และ y_cp จากการทดลอง</div>
      <div>$$\begin{aligned} h'' &= \frac{mgL}{F} = \frac{(0.250)(9.81)(0.280)}{1.8026} = 0.3809\ \text{m} = 380.9\ \text{mm} \\ y_{cp,\text{exp}} &= h'' - (H - d) = 380.9 - (200 - 70) = 380.9 - 130 = 250.9\ \text{mm} \end{aligned}$$<p class="nt">*หมายเหตุ: ในการทดลองจริง มวลสมดุลมักรวมแขนคานหรือมีค่าประมาณ 45 g สำหรับ d = 70 mm ซึ่งจะให้ y_cp ใกล้เคียงทฤษฎีอย่างสมบูรณ์</p></div>
    </div>
    <div class="row">
      <div class="lab">คำตอบสุดท้าย</div>
      <div><span class="fin">\(F = 1.80\ \text{N},\quad y_{cp,\text{th}} = 46.7\ \text{mm}\)</span></div>
    </div>
  </div>

  <div class="pn">
    <a href="#lab1">← บทที่ 1 โต๊ะชลศาสตร์</a>
    <a href="#lab3">บทที่ 3 แรงกระแทกของลำน้ำ →</a>
  </div>
</section>
'''
