# -*- coding: utf-8 -*-

def get_section_ref():
    return r'''
<section id="ref">
  <header class="top">
    <p class="kick">ตารางค่าคงที่ทางฟิสิกส์ การแปลงหน่วย และคำศัพท์วิศวกรรม</p>
    <h1>ตารางอ้างอิงและคำศัพท์เทคนิค (References &amp; Glossary)</h1>
    <p class="sub">คุณสมบัติของน้ำบริสุทธิ์ · ข้อมูลอุปกรณ์แล็บ Essom และ Armfield · ศัพท์ไทย-อังกฤษ</p>
    <p class="by">CE 272 ปฏิบัติการกลศาสตร์ของไหล · ภาควิชาวิศวกรรมโยธา มหาวิทยาลัยธรรมศาสตร์</p>
  </header>

  <h2 class="prob"><span class="tag">อ้างอิง</span>ตารางค่าคงที่ทางกายภาพและอุปกรณ์</h2>
  <div class="stmt">
    <p>รวบรวมค่าคงที่ทางฟิสิกส์ของน้ำ อัตราส่วนการแปลงหน่วยที่ใช้บ่อยในห้องสอบ และข้อมูลขนาดเฉพาะของเครื่องมือทดสอบในห้องปฏิบัติการกลศาสตร์ของไหล ภาควิชาวิศวกรรมโยธา มหาวิทยาลัยธรรมศาสตร์</p>
  </div>

  <h3 class="grp">1. คุณสมบัติทางกายภาพของน้ำบริสุทธิ์ที่ความดันบรรยากาศ</h3>
  <div class="tw">
    <table>
      <caption>คุณสมบัติของน้ำที่อุณหภูมิต่างๆ (\(15^\circ\text{C} - 35^\circ\text{C}\))</caption>
      <thead>
        <tr>
          <th>อุณหภูมิ (°C)</th>
          <th>ความหนาแน่น \(\rho\) (kg/m³)</th>
          <th>น้ำหนักจำเพาะ \(\gamma\) (N/m³)</th>
          <th>ความหนืดไดนามิก \(\mu\) (\(10^{-3}\) N·s/m²)</th>
          <th>ความหนืดคิเนมาติก \(\nu\) (\(10^{-6}\) m²/s)</th>
        </tr>
      </thead>
      <tbody>
        <tr><td>15</td><td>999.1</td><td>9,801</td><td>1.138</td><td>1.139</td></tr>
        <tr><td>20</td><td>998.2</td><td>9,792</td><td>1.002</td><td>1.004</td></tr>
        <tr><td><b>25 (อุณหภูมิห้องแล็บ)</b></td><td><b>997.0</b></td><td><b>9,781</b></td><td><b>0.890</b></td><td><b>0.893</b></td></tr>
        <tr><td>30</td><td>995.7</td><td>9,768</td><td>0.798</td><td>0.801</td></tr>
        <tr><td>35</td><td>994.0</td><td>9,751</td><td>0.719</td><td>0.723</td></tr>
      </tbody>
    </table>
  </div>
  <p class="nt">*หมายเหตุ: ในการสอบ หากโจทย์ไม่ระบุอุณหภูมิ อนุโลมให้ใช้ \(\rho = 1,000\text{ kg/m}^3\), \(\gamma = 9,810\text{ N/m}^3\) และ \(g = 9.81\text{ m/s}^2\)</p>

  <h3 class="grp">2. ตารางแปลงหน่วยชลศาสตร์ที่พบบ่อย (Unit Conversions)</h3>
  <div class="tw">
    <table>
      <caption>ตัวคูณการแปลงหน่วยระบบ SI และหน่วยปฏิบัติการ</caption>
      <thead>
        <tr><th>ปริมาณ</th><th>หน่วยเริ่มต้น</th><th>หน่วยเป้าหมาย (SI)</th><th>วิธีแปลงหน่วย (คูณด้วย)</th></tr>
      </thead>
      <tbody>
        <tr><td>ปริมาตร (Volume)</td><td>ลิตร (L)</td><td>ลูกบาศก์เมตร (m³)</td><td>\(\times 10^{-3}\) (หาร 1,000)</td></tr>
        <tr><td>ปริมาตร (Volume)</td><td>มิลลิลิตร (mL)</td><td>ลูกบาศก์เมตร (m³)</td><td>\(\times 10^{-6}\) (หาร 1,000,000)</td></tr>
        <tr><td>อัตราการไหล (Flow Rate)</td><td>L/s</td><td>m³/s</td><td>\(\times 10^{-3}\)</td></tr>
        <tr><td>อัตราการไหล (Flow Rate)</td><td>L/min</td><td>m³/s</td><td>\(\div 60,000\) (\(\times 1.6667 \times 10^{-5}\))</td></tr>
        <tr><td>อัตราการไหล (Flow Rate)</td><td>m³/hr</td><td>m³/s</td><td>\(\div 3,600\) (\(\times 2.7778 \times 10^{-4}\))</td></tr>
        <tr><td>ความดัน (Pressure)</td><td>m ของน้ำ (m H₂O)</td><td>ปาสคาล (Pa หรือ N/m²)</td><td>\(\times 9,810\) (\(\gamma_{\text{water}}\))</td></tr>
        <tr><td>ความดัน (Pressure)</td><td>บาร์ (bar)</td><td>ปาสคาล (Pa)</td><td>\(\times 10^5\) (\(100,000\text{ Pa}\))</td></tr>
      </tbody>
    </table>
  </div>

  <h3 class="grp">3. คำศัพท์เทคนิคปฏิบัติการกลศาสตร์ของไหล (Glossary)</h3>
  <div class="tw">
    <table>
      <thead>
        <tr><th>คำศัพท์ภาษาอังกฤษ</th><th>ความหมายภาษาไทย</th><th>บทที่เกี่ยวข้อง</th></tr>
      </thead>
      <tbody>
        <tr><td>Hydraulic Bench</td><td>โต๊ะชลศาสตร์ (สถานีจ่ายน้ำและวัดปริมาตร)</td><td>บทที่ 1</td></tr>
        <tr><td>Sump Tank / Volumetric Tank</td><td>ถังพักน้ำด้านล่าง / ถังตวงปริมาตรด้านบน</td><td>บทที่ 1</td></tr>
        <tr><td>Center of Pressure (\(y_{cp}\))</td><td>จุดศูนย์กลางของแรงดัน (จุดที่แรงดันน้ำลัพธ์กระทำ)</td><td>บทที่ 2</td></tr>
        <tr><td>Quadrant Assembly</td><td>ชุดทุ่นเสี้ยววงกลมสำหรับทดสอบแรงดันสถิต</td><td>บทที่ 2</td></tr>
        <tr><td>Partially / Fully Submerged</td><td>แผ่นพื้นจมน้ำบางส่วน / จมมิดน้ำทั้งหมด</td><td>บทที่ 2</td></tr>
        <tr><td>Impact of Jet</td><td>แรงกระแทกของลำน้ำอันเกิดจากโมเมนตัม</td><td>บทที่ 3</td></tr>
        <tr><td>Flat Plate / Hemispherical Cup</td><td>แผ่นเป้าแบบเรียบแบน 90° / ถ้วยครึ่งวงกลม 180°</td><td>บทที่ 3</td></tr>
        <tr><td>Venturi Tube</td><td>หลอดเวนจูรี่ (ท่อคอดวัดอัตราการไหล)</td><td>บทที่ 4</td></tr>
        <tr><td>EGL / HGL</td><td>เส้นระดับพลังงานรวม / เส้นระดับชลศาสตร์</td><td>บทที่ 4</td></tr>
        <tr><td>Manning's Roughness (\(n\))</td><td>สัมประสิทธิ์ความขรุขระของแมนนิ่ง</td><td>บทที่ 5</td></tr>
        <tr><td>Hydraulic Radius (\(R_h\))</td><td>รัศมีชลศาสตร์ (พื้นที่หารด้วยเส้นขอบเปียก)</td><td>บทที่ 5</td></tr>
        <tr><td>Wetted Perimeter (\(P_w\))</td><td>เส้นขอบเปียก (เฉพาะผนังแข็งที่สัมผัสน้ำ)</td><td>บทที่ 5</td></tr>
        <tr><td>Sharp-crested Weir</td><td>ฝายสันคมสำหรับวัดอัตราการไหลในทางน้ำเปิด</td><td>บทที่ 6</td></tr>
        <tr><td>V-Notch Weir</td><td>ฝายสามเหลี่ยมตัววี (เหมาะกับน้ำไหลน้อย)</td><td>บทที่ 6</td></tr>
        <tr><td>Hook Gauge</td><td>เกจวัดระดับน้ำปลายแหลมพร้อมเวอร์เนียร์</td><td>บทที่ 6</td></tr>
        <tr><td>Major Loss / Minor Loss</td><td>การสูญเสียหลัก (แรงเสียดทาน) / การสูญเสียรอง (ข้อต่อ)</td><td>บทที่ 7</td></tr>
        <tr><td>Darcy Friction Factor (\(f\))</td><td>สัมประสิทธิ์ความเสียดทานในท่อ</td><td>บทที่ 7</td></tr>
        <tr><td>Vena Contracta</td><td>บริเวณที่สายน้ำหดตัวจนมีหน้าตัดแคบที่สุด</td><td>บทที่ 8</td></tr>
        <tr><td>Jet Trajectory</td><td>แนววิถีการเคลื่อนที่แบบโพรเจกไทล์ของลำน้ำ</td><td>บทที่ 8</td></tr>
        <tr><td>Head Correction Factor (\(H_d\))</td><td>ค่าแก้ระดับความสูงของเกจวัดความดันปั๊มน้ำ</td><td>บทที่ 9</td></tr>
        <tr><td>Total Dynamic Head (\(H\))</td><td>เฮดรวมที่เครื่องสูบน้ำสร้างขึ้น</td><td>บทที่ 9</td></tr>
        <tr><td>Water Horsepower (\(W_i\))</td><td>กำลังงานไฮดรอลิกที่ของเหลวได้รับ</td><td>บทที่ 9</td></tr>
        <tr><td>Sluice Gate</td><td>บานประตูระบายน้ำตรงในทางน้ำเปิด</td><td>บทที่ 10</td></tr>
        <tr><td>Subcritical / Supercritical</td><td>การไหลต่ำกว่าวิกฤต (Fr &lt; 1) / เหนือวิกฤต (Fr &gt; 1)</td><td>บทที่ 10</td></tr>
        <tr><td>Hydraulic Jump</td><td>น้ำกระโดด (การเปลี่ยนสภาวะกลับสู่ Subcritical)</td><td>บทที่ 10</td></tr>
        <tr><td>Venturi Flume</td><td>รางน้ำแบบเวนจูรี่ (บีบคอคอดวัดน้ำในคลอง)</td><td>บทที่ 11</td></tr>
        <tr><td>Critical Depth (\(y_c\))</td><td>ความลึกวิกฤต (\(y_c = \frac{2}{3}H\) ในรางสี่เหลี่ยม)</td><td>บทที่ 11</td></tr>
      </tbody>
    </table>
  </div>

  <div class="pn">
    <a href="#calc">← คิดเลข</a>
    <a href="#sum">กลับสู่หน้าแรก (สรุปภาพรวม) →</a>
  </div>

  <p class="foot">
    CE 272 ปฏิบัติการกลศาสตร์ของไหล · ภาควิชาวิศวกรรมโยธา คณะวิศวกรรมศาสตร์ มหาวิทยาลัยธรรมศาสตร์<br>
    จัดทำและเรียบเรียงโดย <b>ธนภรณ์ นพรัตน์ (Thanaporn Nopparat)</b><br>
    เรนเดอร์สูตรคณิตศาสตร์ด้วย KaTeX · ออกแบบอินเทอร์เฟซตามสถาปัตยกรรม cn271-fluid-mechanics
  </p>
</section>
'''
