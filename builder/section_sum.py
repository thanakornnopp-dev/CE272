# -*- coding: utf-8 -*-

def get_section_sum():
    return r'''
<section id="sum" class="on">
  <header class="top">
    <p class="kick">แนวทางการเตรียมสอบปฏิบัติการกลศาสตร์ของไหลสำหรับวิศวกรโยธา</p>
    <h1>CE 272 ปฏิบัติการกลศาสตร์ของไหล</h1>
    <p class="sub">สรุปเนื้อหา · สมการควบคุม · ขั้นตอนทดลอง · จุดดักคะแนน ครบทั้ง 11 บท</p>
    <p class="by">ภาควิชาวิศวกรรมโยธา คณะวิศวกรรมศาสตร์ มหาวิทยาลัยธรรมศาสตร์<br>อ้างอิงคู่มือปฏิบัติการและแนวข้อสอบภาควิชา · จัดทำโดย ธนภรณ์ นพรัตน์</p>
    <p class="pracnote">โหมดฝึกเปิดอยู่: ซ่อนวิธีทำไว้ แตะแต่ละขั้นเพื่อดู (ลองเขียนเองก่อน) กดปุ่ม "ฝึก" อีกครั้งเพื่อปิด</p>
  </header>

  <h2 class="prob"><span class="tag">ภาพรวม</span>สรุปมโนทัศน์สำคัญและการสอบปฏิบัติการ</h2>
  <div class="stmt">
    <p>คู่มือนี้สรุปเนื้อหาปฏิบัติการกลศาสตร์ของไหล (CE 272) ครบทั้ง 11 บทตามคู่มือแล็บฉบับเต็มของภาควิชา พร้อมเจาะลึกจุดประสงค์ สมการควบคุม การหักล้างของแรงทางฟิสิกส์ การบันทึกข้อมูล และจุดหลอกที่ข้อสอบชอบดักคะแนน เพื่อให้นักศึกษาสามารถทบทวนและซ้อมทำโจทย์ได้อย่างรวดเร็วและแม่นยำ</p>
  </div>

  <div class="jump">
    <a href="#sum-a">ตาราง 11 บท</a>
    <a href="#sum-b">การ์ดสรุปสูตร 11 บท</a>
    <a href="#sum-c">จุดดักข้อสอบ</a>
    <a href="#lab1">บท 1 โต๊ะน้ำ</a>
    <a href="#lab2">บท 2 จุดแรงดัน</a>
    <a href="#lab3">บท 3 แรงกระแทก</a>
    <a href="#lab4">บท 4 เบอร์นูลี่</a>
    <a href="#lab5">บท 5 แมนนิ่ง</a>
    <a href="#lab6">บท 6 ฝายน้ำ</a>
    <a href="#lab7">บท 7 ท่อสูญเสีย</a>
    <a href="#lab8">บท 8 รูลอด Orifice</a>
    <a href="#lab9">บท 9 ปั๊มน้ำ</a>
    <a href="#lab10">บท 10 ประตูน้ำ</a>
    <a href="#lab11">บท 11 รางเวนจูรี่</a>
    <a href="#exam">คลังข้อสอบ &amp; โหมดฝึก</a>
    <a href="#calc">คิดเลข</a>
    <a href="#ref">ตารางอ้างอิง</a>
  </div>

  <h3 class="grp" id="sum-a">ก. สรุปสมการควบคุมหลักทั้ง 11 บท (Governing Formulas Matrix)</h3>
  <div class="tw">
    <table>
      <caption>ตารางสรุปสมการและแก่นการทดลอง ครบ 11 บท (เลื่อนแนวนอนเพื่อดูคอลัมน์เต็ม)</caption>
      <thead>
        <tr>
          <th class="td-num">บทที่</th>
          <th class="td-name">ชื่อการทดลอง</th>
          <th class="td-eq">สมการสำคัญ</th>
          <th class="td-vars">ตัวแปรหลักที่ต้องหา</th>
          <th class="td-tools">เครื่องมือสำคัญ</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td class="td-num"><b>1</b></td>
          <td class="td-name">โต๊ะชลศาสตร์<small>Hydraulic Bench</small></td>
          <td class="td-eq">
            <div class="eq-row">
              <div class="eq-pill">\(Q = \frac{\Delta V}{\Delta t}\)</div>
              <div class="eq-subnote">\(1\text{ L} = 10^{-3}\text{ m}^3,\quad 1\text{ mL} = 10^{-6}\text{ m}^3\)</div>
            </div>
          </td>
          <td class="td-vars">อัตราการไหลจริง \(Q_{\text{act}}\), เวลา \(\Delta t\)</td>
          <td class="td-tools">ถังตวง Volumetric, นาฬิกาจับเวลา, Sight Glass</td>
        </tr>
        <tr>
          <td class="td-num"><b>2</b></td>
          <td class="td-name">จุดศูนย์กลางแรงดัน<small>Center of Pressure</small></td>
          <td class="td-eq">
            <div class="eq-row">
              <div class="eq-pill">\(F = \gamma h_{cg} A\)</div>
              <div class="eq-pill">\(y_{cp} = y_c + \frac{I_{xx}}{y_c A}\)</div>
              <div class="eq-subnote">ทดลองสมดุลโมเมนต์: \(y_{cp,\text{exp}} = \frac{m g L}{F}\)</div>
            </div>
          </td>
          <td class="td-vars">แรงดัน \(F\), จุดศูนย์กลางแรงดัน \(y_{cp}\), ระดับน้ำ \(d\)</td>
          <td class="td-tools">ทุ่นเสี้ยววงกลม Quadrant, คานถ่วงสมดุล, ตุ้มน้ำหนัก</td>
        </tr>
        <tr>
          <td class="td-num"><b>3</b></td>
          <td class="td-name">แรงกระแทกลำน้ำ<small>Impact of Jet</small></td>
          <td class="td-eq">
            <div class="eq-row">
              <div class="eq-pill">\(F = \rho Q v (\cos\theta + 1)\)</div>
              <div class="eq-subnote"><span class="badge-sm">แผ่นแบน 90°</span> \(F = \rho Q v\) · <span class="badge-sm">ถ้วย 180°</span> \(F = 2 \rho Q v\)</div>
            </div>
          </td>
          <td class="td-vars">แรงกระแทก \(F\), โมเมนตัมลำน้ำ, ความเร็วหัวฉีด \(v\)</td>
          <td class="td-tools">แผ่นเป้า 90° แบน vs ถ้วย 180° ครึ่งวงกลม, สปริงถ่วง</td>
        </tr>
        <tr>
          <td class="td-num"><b>4</b></td>
          <td class="td-name">สมการเบอร์นูลี่<small>Bernoulli &amp; Venturi</small></td>
          <td class="td-eq">
            <div class="eq-row">
              <div class="eq-pill">\(\frac{P_1}{\gamma} + \frac{v_1^2}{2g} + z_1 = \frac{P_2}{\gamma} + \frac{v_2^2}{2g} + z_2\)</div>
              <div class="eq-pill">\(C_d = \frac{Q_{\text{act}}}{Q_{\text{th}}},\quad Q_{\text{th}} = A_1 \sqrt{\frac{2g \Delta h}{(A_1/A_2)^2 - 1}}\)</div>
            </div>
          </td>
          <td class="td-vars">\(Q_{\text{th}}, Q_{\text{act}}, C_d\), เส้น EGL/HGL</td>
          <td class="td-tools">หลอดเวนจูรี่, มาโนมิเตอร์หลายหลอด, ปั๊มลม</td>
        </tr>
        <tr>
          <td class="td-num"><b>5</b></td>
          <td class="td-name">สมการแมนนิ่ง<small>Manning's Flow</small></td>
          <td class="td-eq">
            <div class="eq-row">
              <div class="eq-pill">\(V = \frac{1}{n} R_h^{2/3} S_0^{1/2}\)</div>
              <div class="eq-pill">\(Q = V A = \frac{1}{n} A R_h^{2/3} S_0^{1/2},\quad R_h = \frac{A}{P_w}\)</div>
            </div>
          </td>
          <td class="td-vars">ความขรุขระ \(n\), รัศมีชลศาสตร์ \(R_h\), ความลาดชัน \(S_0\)</td>
          <td class="td-tools">รางน้ำเปิดปรับเอียง, แผ่นหญ้าเทียมขรุขระ, Point Gauge</td>
        </tr>
        <tr>
          <td class="td-num"><b>6</b></td>
          <td class="td-name">การวัดด้วยฝาย<small>Weir Flow</small></td>
          <td class="td-eq">
            <div class="eq-row">
              <div class="eq-pill"><span class="badge-sm">ฝายสี่เหลี่ยม</span> \(Q = \frac{2}{3} C_d b \sqrt{2g} H^{1.5}\)</div>
              <div class="eq-pill"><span class="badge-sm">ฝายสามเหลี่ยม 90°</span> \(Q = \frac{8}{15} C_d \sqrt{2g} \tan(\frac{\theta}{2}) H^{2.5}\)</div>
            </div>
          </td>
          <td class="td-vars">\(Q_{\text{th}}, C_d\), กราฟลอการิทึม (\(\log Q\) vs \(\log H\))</td>
          <td class="td-tools">ฝายสันคม, Hook Gauge วัดระดับน้ำ</td>
        </tr>
        <tr>
          <td class="td-num"><b>7</b></td>
          <td class="td-name">การสูญเสียในท่อ<small>Pipe Losses</small></td>
          <td class="td-eq">
            <div class="eq-row">
              <div class="eq-pill">\(h_f = f \frac{L}{D} \frac{v^2}{2g} = \frac{8 f L Q^2}{\pi^2 g D^5}\)</div>
              <div class="eq-pill">\(h_m = K \frac{v^2}{2g}\)</div>
              <div class="eq-subnote">ท่ออนุกรม: \(h_L = h_1 + h_2\) · ท่อขนาน: \(h_{L,1} = h_{L,2},\ Q = Q_1 + Q_2\)</div>
            </div>
          </td>
          <td class="td-vars">Friction \(f\), ค่า \(K\), เฮดสูญเสียแบบขนาน/อนุกรม</td>
          <td class="td-tools">แผงโครงข่ายท่อ A, B, C, D, มาโนมิเตอร์ปรอท/น้ำ</td>
        </tr>
        <tr>
          <td class="td-num"><b>8</b></td>
          <td class="td-name">การไหลผ่านรูลอด<small>Orifice &amp; Jet</small></td>
          <td class="td-eq">
            <div class="eq-row">
              <div class="eq-pill">\(v_{\text{th}} = \sqrt{2gH},\quad x = 2 C_v \sqrt{y H}\)</div>
              <div class="eq-pill">\(C_d = C_v \times C_c = \frac{Q_{\text{act}}}{A_0 \sqrt{2gH}}\)</div>
            </div>
          </td>
          <td class="td-vars">\(C_v, C_c, C_d\), แนววิถีลำน้ำพิกัด \((x, y)\)</td>
          <td class="td-tools">ถังน้ำระดับคงที่ Constant Head, แผงเข็มวัดพิกัดลำน้ำ</td>
        </tr>
        <tr>
          <td class="td-num"><b>9</b></td>
          <td class="td-name">ทดสอบปั๊มน้ำ<small>Pump Test</small></td>
          <td class="td-eq">
            <div class="eq-row">
              <div class="eq-pill">\(H = (h_2 - h_1) + H_d\)</div>
              <div class="eq-pill">\(W_i = \gamma Q H,\quad \eta_o = \frac{W_i}{W_m} \times 100\%\)</div>
              <div class="eq-subnote">ปั๊มเดี่ยว: \(H_d = +0.15\text{ m}\) · อนุกรม: \(H_d = -0.07\text{ m}\) · ขนาน: \(H_d = +0.94\text{ m}\)</div>
            </div>
          </td>
          <td class="td-vars">Total Head \(H\), กำลังน้ำ \(W_i\), ประสิทธิภาพ \(\eta_o\)</td>
          <td class="td-tools">ปั๊มเดี่ยว/อนุกรม/ขนาน, เกจความดันดูด-ส่ง, วัตต์มิเตอร์</td>
        </tr>
        <tr>
          <td class="td-num"><b>10</b></td>
          <td class="td-name">ไหลลอดประตูน้ำ<small>Sluice Gate</small></td>
          <td class="td-eq">
            <div class="eq-row">
              <div class="eq-pill">\(E = y + \frac{v^2}{2g},\quad Fr = \frac{V}{\sqrt{g y}}\)</div>
              <div class="eq-pill">\(Q = C_d y_g B \sqrt{2g y_0}\)</div>
            </div>
          </td>
          <td class="td-vars">พลังงานจำเพาะ \(E\), Froude Number \(Fr\), ความลึกวิกฤต \(y_c\)</td>
          <td class="td-tools">บานประตูน้ำตรง, Current meter วัดความเร็ว, Point Gauge</td>
        </tr>
        <tr>
          <td class="td-num"><b>11</b></td>
          <td class="td-name">รางเวนจูรี่<small>Venturi Flume</small></td>
          <td class="td-eq">
            <div class="eq-row">
              <div class="eq-pill">\(y_c = \frac{2}{3} y_1,\quad V_c = \sqrt{g y_c}\)</div>
              <div class="eq-pill">\(Q = \left(\frac{2}{3}\right)^{1.5} \sqrt{g}\, b\, y_1^{1.5}\)</div>
            </div>
          </td>
          <td class="td-vars">Critical depth \(y_c\), Free vs Submerged (\(y_3/y_1\))</td>
          <td class="td-tools">รางน้ำบีบหน้าตัดคอคอดในทางน้ำเปิด, Point Gauge</td>
        </tr>
      </tbody>
    </table>
  </div>

  <h3 class="grp" id="sum-b">ข. บัตรสรุปสูตรและการใช้งานประจำบท (Formula Study Cards)</h3>
  <p class="stmt">การ์ดสรุปสูตรสำหรับการท่องจำก่อนเข้าห้องสอบ ทุกสูตรแสดงครบทั้งตัวแปร หน่วย และข้อควรระวัง:</p>
  
  <div class="formula-grid">
    <div class="formula-card">
      <div class="formula-card-head">
        <span class="formula-card-title">บทที่ 1 โต๊ะชลศาสตร์</span>
        <span class="formula-card-badge">LAB 01</span>
      </div>
      <div class="formula-card-body">
        \(Q = \frac{\Delta V}{\Delta t} = \frac{\text{Mass}}{\rho \cdot \Delta t}\)
      </div>
      <div class="formula-card-desc">
        อัตราการไหลโดยปริมาตร วัดจากการจับเวลาน้ำสะสมในถังตวง volumetric
      </div>
      <div class="formula-card-trap">
        ⚠️ แปลงหน่วยลิตรเป็นลูกบาศก์เมตรเสมอ: \(1\text{ L} = 10^{-3}\text{ m}^3\), \(1\text{ m}^3/\text{hr} = \frac{1}{3600}\text{ m}^3/\text{s}\)
      </div>
    </div>

    <div class="formula-card">
      <div class="formula-card-head">
        <span class="formula-card-title">บทที่ 2 จุดศูนย์กลางแรงดัน</span>
        <span class="formula-card-badge">LAB 02</span>
      </div>
      <div class="formula-card-body">
        \(F = \gamma h_{cg} A,\quad y_{cp} = y_c + \frac{I_{xx}}{y_c A}\)
      </div>
      <div class="formula-card-desc">
        แรงดันไฮโดรสแตติกกระทำตั้งฉากกับผิวระนาบเสมอ โดยจุดศูนย์กลางแรงดัน \(y_{cp}\) จะอยู่ต่ำกว่าเซนทรอยด์เสมอ
      </div>
      <div class="formula-card-trap">
        ⚠️ จมมิด: \(y_c = d - D/2\), \(I_{xx} = \frac{B D^3}{12}\) | จมบางส่วน: \(y_c = d/2\), \(I_{xx} = \frac{B d^3}{12}\)
      </div>
    </div>

    <div class="formula-card">
      <div class="formula-card-head">
        <span class="formula-card-title">บทที่ 3 แรงกระแทกลำน้ำ</span>
        <span class="formula-card-badge">LAB 03</span>
      </div>
      <div class="formula-card-body">
        \(F_{\text{flat}} = \rho Q v,\quad F_{\text{hemi}} = 2 \rho Q v\)
      </div>
      <div class="formula-card-desc">
        สมดุลโมเมนตัมลำน้ำ: ถ้วยครึ่งวงกลมสะท้อนน้ำย้อนกลับ \(180^\circ\) ทำให้แรงเป็น 2 เท่าของแผ่นแบนเสมอ
      </div>
      <div class="formula-card-trap">
        ⚠️ ห้ามลืมคูณแรงโน้มถ่วง: \(F_{\text{meas}} = m \cdot g\) (เช่น มวล \(500\text{ g} = 0.5\text{ kg} \implies F = 4.905\text{ N}\))
      </div>
    </div>

    <div class="formula-card">
      <div class="formula-card-head">
        <span class="formula-card-title">บทที่ 4 สมการเบอร์นูลี่</span>
        <span class="formula-card-badge">LAB 04</span>
      </div>
      <div class="formula-card-body">
        \(\frac{P_1}{\gamma} + \frac{v_1^2}{2g} + z_1 = \frac{P_2}{\gamma} + \frac{v_2^2}{2g} + z_2\)
      </div>
      <div class="formula-card-desc">
        พลังงานรวมคงที่เมื่อไม่มีการสูญเสีย จุดคอคอดความเร็วสูงสุดแต่ความดันต่ำสุดตามผลเวนจูรี่
      </div>
      <div class="formula-card-trap">
        ⚠️ \(Q_{\text{th}} = A_1 \sqrt{\frac{2g\Delta h}{(A_1/A_2)^2 - 1}}\), \(C_d = \frac{Q_{\text{act}}}{Q_{\text{th}}} < 1.0\) เสมอ
      </div>
    </div>

    <div class="formula-card">
      <div class="formula-card-head">
        <span class="formula-card-title">บทที่ 5 สมการแมนนิ่ง</span>
        <span class="formula-card-badge">LAB 05</span>
      </div>
      <div class="formula-card-body">
        \(V = \frac{1}{n} R_h^{2/3} S_0^{1/2},\quad R_h = \frac{A}{P_w} = \frac{by}{b+2y}\)
      </div>
      <div class="formula-card-desc">
        การไหลสม่ำเสมอในทางน้ำเปิด ค่าสัมประสิทธิ์ความขรุขระ \(n\) ของหญ้าเทียม (\(\approx 0.016-0.022\)) สูงกว่าผิวเรียบ
      </div>
      <div class="formula-card-trap">
        ⚠️ \(P_w\) คิดเฉพาะขอบเปียกน้ำ (ก้นราง + 2 ข้างผนัง) ไม่รวมผิวน้ำด้านบนเด็ดขาด!
      </div>
    </div>

    <div class="formula-card">
      <div class="formula-card-head">
        <span class="formula-card-title">บทที่ 6 การวัดการไหลด้วยฝาย</span>
        <span class="formula-card-badge">LAB 06</span>
      </div>
      <div class="formula-card-body">
        \(Q_{\text{rect}} = \frac{2}{3} C_d b \sqrt{2g} H^{1.5},\quad Q_{\text{tri}} = \frac{8}{15} C_d \sqrt{2g} \tan\left(\frac{\theta}{2}\right) H^{2.5}\)
      </div>
      <div class="formula-card-desc">
        ฝายสี่เหลี่ยมเหมาะกับน้ำมาก (\(Q \propto H^{1.5}\)) ส่วนฝายสามเหลี่ยม 90° แม่นยำกับน้ำน้อย (\(Q \propto H^{2.5}\))
      </div>
      <div class="formula-card-trap">
        ⚠️ กราฟ \(\log Q\) vs \(\log H\): ความชันสี่เหลี่ยมต้อง \(\approx 1.5\) และสามเหลี่ยมต้อง \(\approx 2.5\)
      </div>
    </div>

    <div class="formula-card">
      <div class="formula-card-head">
        <span class="formula-card-title">บทที่ 7 การสูญเสียในท่อ</span>
        <span class="formula-card-badge">LAB 07</span>
      </div>
      <div class="formula-card-body">
        \(h_f = f \frac{L}{D}\frac{v^2}{2g} = \frac{8 f L Q^2}{\pi^2 g D^5},\quad h_m = K \frac{v^2}{2g}\)
      </div>
      <div class="formula-card-desc">
        เฮดสูญเสียจากความฝืดแปรผันตาม \(1/D^5\) ท่อขนาดเล็กสูญเสียมากกว่าท่อใหญ่หลายเท่าตัว
      </div>
      <div class="formula-card-trap">
        ⚠️ ท่อขนาน: \(h_L\) เท่ากัน อัตราการไหลรวม \(Q = Q_A + Q_B\) โดยท่อโตส่งน้ำได้มากกว่าตามสัดส่วน \(D^{2.5}\)
      </div>
    </div>

    <div class="formula-card">
      <div class="formula-card-head">
        <span class="formula-card-title">บทที่ 8 การไหลผ่านรูลอด</span>
        <span class="formula-card-badge">LAB 08</span>
      </div>
      <div class="formula-card-body">
        \(v_{\text{th}} = \sqrt{2gH},\quad C_v = \frac{x}{2\sqrt{yH}},\quad C_d = C_v \times C_c\)
      </div>
      <div class="formula-card-desc">
        การวัดพิกัดแนววิถีพาราโบลา \((x, y)\) เพื่อหาสัมประสิทธิ์ความเร็ว \(C_v \approx 0.97\) และการคอดตัว \(C_c \approx 0.64\)
      </div>
      <div class="formula-card-trap">
        ⚠️ ระวังค่า \(C_d = C_v \times C_c \approx 0.60-0.64\) ถ้าคำนวณได้เกิน 1.0 แสดงว่าใส่พิกัด \(x, y\) สลับกัน
      </div>
    </div>

    <div class="formula-card">
      <div class="formula-card-head">
        <span class="formula-card-title">บทที่ 9 การทดสอบปั๊มน้ำ</span>
        <span class="formula-card-badge">LAB 09</span>
      </div>
      <div class="formula-card-body">
        \(H = (h_2 - h_1) + H_d,\quad W_i = \gamma Q H,\quad \eta_o = \frac{W_i}{W_m} \times 100\%\)
      </div>
      <div class="formula-card-desc">
        สมรรถนะปั๊มหอยโข่ง: การต่ออนุกรมเพื่อเพิ่มเฮด (\(H_{\text{total}} = 2H\)) และต่อขนานเพื่อเพิ่มการไหล (\(Q_{\text{total}} = 2Q\))
      </div>
      <div class="formula-card-trap">
        ⚠️ ปั๊มอนุกรม: \(H_d = -0.07\text{ m}\) (ติดลบเพราะดูดจากถังพักเปิด \(h_1 = 0\)) ลืมลบคำตอบผิดทันที!
      </div>
    </div>

    <div class="formula-card">
      <div class="formula-card-head">
        <span class="formula-card-title">บทที่ 10 ประตูน้ำ &amp; พลังงานจำเพาะ</span>
        <span class="formula-card-badge">LAB 10</span>
      </div>
      <div class="formula-card-body">
        \(E = y + \frac{v^2}{2g},\quad Fr = \frac{V}{\sqrt{gy}},\quad Q = C_d y_g B \sqrt{2g y_0}\)
      </div>
      <div class="formula-card-desc">
        ต้นน้ำก่อนลอดประตูเป็น Subcritical (\(Fr < 1\)) ท้ายน้ำลอดประตูเป็น Supercritical (\(Fr > 1\)) จนเกิด Hydraulic Jump
      </div>
      <div class="formula-card-trap">
        ⚠️ \(E_{\min} = 1.5 y_c\) สำหรับทางน้ำเปิดรูปสี่เหลี่ยมผืนผ้า ที่สภาวะวิกฤต \(Fr = 1.0\)
      </div>
    </div>

    <div class="formula-card">
      <div class="formula-card-head">
        <span class="formula-card-title">บทที่ 11 รางเวนจูรี่</span>
        <span class="formula-card-badge">LAB 11</span>
      </div>
      <div class="formula-card-body">
        \(y_c = \frac{2}{3} y_1,\quad Q = \left(\frac{2}{3}\right)^{1.5} \sqrt{g}\, b\, y_1^{1.5}\)
      </div>
      <div class="formula-card-desc">
        การวัดอัตราการไหลในทางน้ำเปิดโดยการบีบหน้าตัดคอคอด ที่คอคอดระดับน้ำจะลดลงสู่สภาวะวิกฤต \(y_c\)
      </div>
      <div class="formula-card-trap">
        ⚠️ สภาวะไหลอิสระ (Free Flow) เกิดขึ้นเมื่ออัตราส่วนระดับน้ำจม \(y_3/y_1 < 0.80\) เท่านั้น
      </div>
    </div>
  </div>

  <h3 class="grp" id="sum-c">ค. จุดดักคะแนนและข้อควรระวังในห้องสอบ (Critical Exam Traps)</h3>
  <div class="bx trap">
    <b>กับดักหน่วยยกกำลังสิบ (The 10^X Unit Trap):</b>
    <div>
      ในข้อสอบอาจารย์มักให้ปริมาตรน้ำเป็น <b>ลิตร (L)</b> หรือ <b>มิลลิลิตร (mL)</b> และเวลาเป็น <b>วินาที (s)</b> หรือ <b>นาที (min)</b><br>
      • ห้ามนำค่าลิตรไปคูณกับความเร่งโน้มถ่วงหรือความหนาแน่นตรงๆ เด็ดขาด!<br>
      • กฎเหล็ก: แปลงเป็นหน่วย SI เสมอ: \(1\text{ L} = 10^{-3}\text{ m}^3\), \(1\text{ mL} = 10^{-6}\text{ m}^3\)<br>
      • เช่น \(Q = 12\text{ L/min} \implies Q = \frac{12 \times 10^{-3}}{60} = 2.0 \times 10^{-4}\text{ m}^3/\text{s}\)
    </div>
  </div>

  <div class="bx trap">
    <b>กับดักค่าแก้ระดับความสูงเกจปั๊มน้ำ (Datum Head Correction \(H_d\)):</b>
    <div>
      สมการหาเฮดรวมของปั๊มคือ \(H = (h_2 - h_1) + H_d\)<br>
      • <b>ปั๊มเดี่ยว:</b> \(H_d = +0.15\text{ m}\)<br>
      • <b>ปั๊มต่ออนุกรม:</b> น้ำดูดจากถังพักเปิด \(h_1 = 0\) และ \(H_d = -0.07\text{ m}\) <b>(ค่าติดลบ! ลืมใส่เครื่องหมายลบคะแนนหายทันที)</b><br>
      • <b>ปั๊มต่อขนาน:</b> ส่งรวมเข้าท่อ Manifold ด้านบน \(H_d = +0.94\text{ m}\)
    </div>
  </div>

  <h3 class="grp" id="sum-d">ง. การตรวจสอบสภาวะทางฟิสิกส์ (Physical Reality Checks)</h3>
  <div class="bx chk">
    <b>การตรวจสอบความสมเหตุสมผลทางฟิสิกส์ (Reality Checks Checklist):</b>
    <div>
      • ค่าสัมประสิทธิ์การไหล \(C_d\), \(C_v\), \(C_c\) ต้องน้อยกว่า 1.0 เสมอ (ปกติ \(C_d \approx 0.60 - 0.98\)) ถ้าคำนวณได้เกิน 1 แสดงว่าสลับเศษส่วนหรือลืมแปลงหน่วย<br>
      • แรงกระแทกบนถ้วยครึ่งวงกลม (\(180^\circ\)) ต้องเป็น <b>2 เท่า</b> ของแผ่นเรียบแบนเสมอ (\(F_{\text{hemi}} = 2 F_{\text{flat}}\)) เพราะโมเมนตัมสะท้อนกลับทิศ \(180^\circ\)<br>
      • จุดศูนย์กลางแรงดัน \(y_{cp}\) ต้องอยู่ต่ำกว่าจุดเซนทรอยด์ \(y_c\) เสมอ (\(y_{cp} > y_c\))
    </div>
  </div>

  <div class="pn">
    <span></span>
    <a href="#lab1">บทที่ 1 โต๊ะชลศาสตร์ →</a>
  </div>
</section>
'''
