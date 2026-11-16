# -*- coding: utf-8 -*-

def get_section_calc():
    return r'''
<section id="calc">
  <header class="top">
    <p class="kick">เครื่องมือคำนวณสดสำหรับปฏิบัติการกลศาสตร์ของไหล</p>
    <h1>เครื่องคิดเลขแล็บ (Universal Lab Calculator)</h1>
    <p class="sub">คำนวณอัตราการไหล · จุดศูนย์กลางแรงดัน · แรงกระแทก · ปั๊มน้ำ · ฝาย · รูลอด</p>
    <p class="by">CE 272 ปฏิบัติการกลศาสตร์ของไหล · มหาวิทยาลัยธรรมศาสตร์</p>
  </header>

  <h2 class="prob"><span class="tag">คิดเลข</span>คำนวณและตรวจสอบผลการทดลอง</h2>
  <div class="stmt">
    <p>เครื่องคิดเลขนี้ออกแบบมาเพื่อให้นักศึกษาใช้ตรวจสอบความถูกต้องของรายการคำนวณในเล่มรายงาน และใช้ฝึกทำโจทย์เตรียมสอบ โดยคำนวณตามสมการมาตรฐานของคู่มือปฏิบัติการ CE 272 พร้อมแสดงหน่วยและคำอธิบายอย่างละเอียด</p>
  </div>

  <form id="calcform" class="calc" style="border:1.5px solid var(--ink);padding:18px;background:var(--hover);">
    <div class="full">
      <label>
        <b>เลือกการทดลองที่ต้องการคำนวณ:</b>
        <select name="mode" style="font-weight:600;color:var(--navy);">
          <option value="bench">บทที่ 1: อัตราการไหลโต๊ะชลศาสตร์ (Q = ΔV / Δt)</option>
          <option value="cp">บทที่ 2: จุดศูนย์กลางของแรงดัน (Center of Pressure)</option>
          <option value="jet">บทที่ 3: แรงกระแทกของลำน้ำ (Impact of Jet)</option>
          <option value="venturi">บทที่ 4: สมการเบอร์นูลี่ &amp; ท่อเวนจูรี่ (Venturi Meter)</option>
          <option value="manning">บทที่ 5: สมการแมนนิ่งทางน้ำเปิด (Manning's Flow)</option>
          <option value="weir">บทที่ 6: การวัดอัตราการไหลด้วยฝาย (Flow over Weir)</option>
          <option value="orifice">บทที่ 8: การไหลผ่านรูลอดและวิถีลำน้ำ (Orifice &amp; Trajectory)</option>
          <option value="pump">บทที่ 9: การทดสอบเครื่องสูบน้ำ (Pump Test &amp; Datum Hd)</option>
          <option value="sluice">บทที่ 10: การไหลลอดประตูน้ำ (Sluice Gate)</option>
          <option value="flume">บทที่ 11: รางน้ำแบบเวนจูรี่ (Venturi Flume)</option>
        </select>
      </label>
    </div>

    <!-- Mode: bench -->
    <div data-m="bench">
      <label>ปริมาตรน้ำ (Volume):
        <input type="number" step="any" name="b_vol" value="20" placeholder="เช่น 20">
      </label>
    </div>
    <div data-m="bench">
      <label>หน่วยปริมาตร:
        <select name="b_vol_unit">
          <option value="L">ลิตร (L)</option>
          <option value="mL">มิลลิลิตร (mL)</option>
          <option value="m3">ลูกบาศก์เมตร (m³)</option>
        </select>
      </label>
    </div>
    <div data-m="bench">
      <label>เวลาที่ใช้ (วินาที):
        <input type="number" step="any" name="b_time" value="35" placeholder="เช่น 35">
      </label>
    </div>

    <!-- Mode: cp -->
    <div data-m="cp">
      <label>ระดับความลึกน้ำ d (cm):
        <input type="number" step="any" name="cp_d" value="7.0" placeholder="เช่น 7.0">
      </label>
    </div>
    <div data-m="cp">
      <label>ความสูงแผ่น D (cm, ปกติ 10):
        <input type="number" step="any" name="cp_D" value="10.0">
      </label>
    </div>
    <div data-m="cp">
      <label>ความกว้างแผ่น B (cm, ปกติ 7.5):
        <input type="number" step="any" name="cp_B" value="7.5">
      </label>
    </div>
    <div data-m="cp">
      <label>ระยะคาน L (cm, Essom=28, Armfield=27.5):
        <input type="number" step="any" name="cp_L" value="28.0">
      </label>
    </div>
    <div data-m="cp">
      <label>มวลตุ้มน้ำหนัก m (กรัม, ถ้ามี):
        <input type="number" step="any" name="cp_m" value="45" placeholder="เช่น 45">
      </label>
    </div>

    <!-- Mode: jet -->
    <div data-m="jet">
      <label>อัตราการไหล Q (L/s):
        <input type="number" step="any" name="jet_q" value="0.5" placeholder="เช่น 0.5">
      </label>
    </div>
    <div data-m="jet">
      <label>ขนาดหัวฉีด Nozzle D (mm):
        <input type="number" step="any" name="jet_d" value="8.0">
      </label>
    </div>
    <div data-m="jet">
      <label>ชนิดของฉากกั้น (Vane):
        <select name="jet_target">
          <option value="90">แผ่นเรียบแบน 90° (Flat Plate)</option>
          <option value="0">ถ้วยครึ่งวงกลม 180° (Hemispherical Cup)</option>
          <option value="30">ฉากเอียง 30°</option>
          <option value="120">ฉากเอียง 120°</option>
        </select>
      </label>
    </div>

    <!-- Mode: venturi -->
    <div data-m="venturi">
      <label>เส้นผ่านศูนย์กลางทางเข้า D1 (cm):
        <input type="number" step="any" name="v_d1" value="2.6">
      </label>
    </div>
    <div data-m="venturi">
      <label>เส้นผ่านศูนย์กลางคอคอด D2 (cm):
        <input type="number" step="any" name="v_d2" value="1.6">
      </label>
    </div>
    <div data-m="venturi">
      <label>ผลต่างระดับน้ำ h1 - h2 (cm):
        <input type="number" step="any" name="v_dh" value="18.5">
      </label>
    </div>
    <div data-m="venturi">
      <label>อัตราการไหลจริง Q_act (L/s, ถ้ามี):
        <input type="number" step="any" name="v_qact" value="0.34">
      </label>
    </div>

    <!-- Mode: manning -->
    <div data-m="manning">
      <label>ความกว้างคลอง B (m):
        <input type="number" step="any" name="m_b" value="0.30">
      </label>
    </div>
    <div data-m="manning">
      <label>ความลึกน้ำ y (m):
        <input type="number" step="any" name="m_y" value="0.045">
      </label>
    </div>
    <div data-m="manning">
      <label>ความลาดชันท้องคลอง S0 (tan θ):
        <input type="number" step="any" name="m_s" value="0.00436" placeholder="เช่น tan(0.25°)=0.00436">
      </label>
    </div>
    <div data-m="manning">
      <label>สัมประสิทธิ์ความขรุขระ Manning n:
        <input type="number" step="any" name="m_n" value="0.012">
      </label>
    </div>

    <!-- Mode: weir -->
    <div data-m="weir">
      <label>ชนิดของฝาย:
        <select name="w_type">
          <option value="vnotch">ฝายสามเหลี่ยม 90° (V-Notch)</option>
          <option value="rect">ฝายสันคมสี่เหลี่ยม (Rectangular)</option>
        </select>
      </label>
    </div>
    <div data-m="weir">
      <label>ความสูงน้ำเหนือสันฝาย H (cm):
        <input type="number" step="any" name="w_h" value="6.5">
      </label>
    </div>
    <div data-m="weir">
      <label>ความกว้างฝาย B (cm, เฉพาะฝายสี่เหลี่ยม):
        <input type="number" step="any" name="w_b" value="15.0">
      </label>
    </div>
    <div data-m="weir">
      <label>สัมประสิทธิ์การไหล Cd (ปกติ 0.60):
        <input type="number" step="any" name="w_cd" value="0.60">
      </label>
    </div>

    <!-- Mode: orifice -->
    <div data-m="orifice">
      <label>เฮดระดับน้ำคงที่ H (m):
        <input type="number" step="any" name="o_h" value="0.40">
      </label>
    </div>
    <div data-m="orifice">
      <label>ระยะตกราบ x (m):
        <input type="number" step="any" name="o_x" value="0.35">
      </label>
    </div>
    <div data-m="orifice">
      <label>ระยะตกลงแนวดิ่ง y (m):
        <input type="number" step="any" name="o_y" value="0.08">
      </label>
    </div>
    <div data-m="orifice">
      <label>ขนาดรูเจาะ d0 (mm):
        <input type="number" step="any" name="o_d0" value="10.0">
      </label>
    </div>
    <div data-m="orifice">
      <label>ขนาด Vena Contracta dc (mm, ถ้ามี):
        <input type="number" step="any" name="o_dc" value="8.0">
      </label>
    </div>

    <!-- Mode: pump -->
    <div data-m="pump">
      <label>รูปแบบการต่อปั๊ม:
        <select name="p_config">
          <option value="single">ปั๊มเดี่ยว (Single: Hd = +0.15 m)</option>
          <option value="series">ปั๊มต่ออนุกรม (Series: h1 = 0, Hd = -0.07 m)</option>
          <option value="parallel">ปั๊มต่อขนาน (Parallel: Hd = +0.94 m)</option>
        </select>
      </label>
    </div>
    <div data-m="pump">
      <label>เฮดเกจท่อส่งออก h0 หรือ hm (m):
        <input type="number" step="any" name="p_h2" value="14.8">
      </label>
    </div>
    <div data-m="pump">
      <label>เฮดเกจท่อดูดเข้า h1 (m, ถ้าเป็นอนุกรมจะเป็น 0):
        <input type="number" step="any" name="p_h1" value="0.0">
      </label>
    </div>
    <div data-m="pump">
      <label>อัตราการไหล Q (L/s):
        <input type="number" step="any" name="p_q" value="0.78">
      </label>
    </div>
    <div data-m="pump">
      <label>กำลังไฟฟ้ามอเตอร์ Wm (Watts, ถ้ามี):
        <input type="number" step="any" name="p_wm" value="250">
      </label>
    </div>

    <!-- Mode: sluice -->
    <div data-m="sluice">
      <label>ระดับน้ำต้นน้ำ y0 (m):
        <input type="number" step="any" name="s_y0" value="0.45">
      </label>
    </div>
    <div data-m="sluice">
      <label>ระยะยกบานประตูน้ำ yg (m):
        <input type="number" step="any" name="s_yg" value="0.05">
      </label>
    </div>
    <div data-m="sluice">
      <label>ระดับน้ำท้ายน้ำที่หดตัว y1 (m):
        <input type="number" step="any" name="s_y1" value="0.031">
      </label>
    </div>
    <div data-m="sluice">
      <label>ความกว้างคลอง B (m):
        <input type="number" step="any" name="s_b" value="0.50">
      </label>
    </div>

    <!-- Mode: flume -->
    <div data-m="flume">
      <label>ความกว้างคอคอด b (m):
        <input type="number" step="any" name="f_b" value="0.15">
      </label>
    </div>
    <div data-m="flume">
      <label>ความลึกน้ำต้นน้ำ y1 (m):
        <input type="number" step="any" name="f_y1" value="0.20">
      </label>
    </div>

    <div class="full" style="margin-top:10px;">
      <button type="submit" class="run">คำนวณผลลัพธ์ (Calculate)</button>
    </div>
  </form>

  <div id="calcout" class="calcout"></div>

  <div class="pn">
    <a href="#exam">← คลังข้อสอบ &amp; โหมดฝึก</a>
    <a href="#ref">ตารางอ้างอิง &amp; คำศัพท์ →</a>
  </div>
</section>
'''
