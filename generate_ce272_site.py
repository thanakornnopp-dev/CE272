# -*- coding: utf-8 -*-
"""
Script to build the CE 272 Fluid Mechanics Laboratory Master Study Portal.
Follows the exact design tokens, typography, and UX architecture of cn271-fluid-mechanics.
Ensures 100% Thai font accuracy (zero corrupted OCR characters),
covers all 11 chapters from the lab manual faithfully,
and integrates KaTeX, Practice Mode, and Multi-Lab Calculator.
"""

import os
import re

OUT_FILE = "/Users/thanaporn/.gemini/antigravity/scratch/CE272/index.html"

parts = []

# --- 1. HTML HEAD & SETUP ---
parts.append(r'''<!doctype html>
<html lang="th" data-theme="light">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>CE 272 ปฏิบัติการกลศาสตร์ของไหล ครบ 11 บท · ธรรมศาสตร์</title>
  <meta name="description" content="คู่มือเตรียมสอบและสรุปเนื้อหาปฏิบัติการกลศาสตร์ของไหล CE 272 ฉบับสมบูรณ์ครบทั้ง 11 บท พร้อมสูตร ที่มา วิธีทดลอง จุดดักข้อสอบ และโหมดฝึกทำโจทย์">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Sarabun:ital,wght@0,400;0,500;0,600;0,700;1,400&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/KaTeX/0.16.9/katex.min.css">
  <link rel="stylesheet" href="assets/style.css">
  <script>
    (function(){
      var t = null;
      try { t = localStorage.getItem('theme'); } catch(e){}
      if (t !== 'light' && t !== 'dark') {
        t = matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light';
      }
      document.documentElement.setAttribute('data-theme', t);
    })();
  </script>
</head>
<body>

<!-- Global SVG Defs -->
<svg width="0" height="0" style="position:absolute" aria-hidden="true">
  <defs>
    <marker id="ar" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse">
      <path d="M0 0L10 5L0 10z" fill="context-stroke"/>
    </marker>
  </defs>
</svg>

<!-- Sticky Top Navigation -->
<nav class="toc" aria-label="สารบัญนำทาง">
  <a href="#sum" aria-current="page">สรุปภาพรวม</a>
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
  <a href="#exam" class="gap">คลังข้อสอบ &amp; โหมดฝึก</a>
  <a href="#calc" class="gap">คิดเลข</a>
  <a href="#ref">ตาราง &amp; คำศัพท์</a>
  <span class="sp"></span>
  <span class="tools">
    <button class="th" id="practice" type="button" aria-pressed="false" aria-label="โหมดฝึก ซ่อนวิธีทำ">
      <svg viewBox="0 0 24 24" aria-hidden="true"><path d="M4 20h4L19 9l-4-4L4 16z"/><path d="M13.5 6.5l4 4"/></svg>
      <span class="lbl">ฝึก</span>
    </button>
    <button class="th" id="theme" type="button" aria-label="สลับโหมดสว่าง/มืด">
      <svg class="sun" viewBox="0 0 24 24" aria-hidden="true"><circle cx="12" cy="12" r="4"/><path d="M12 2v2M12 20v2M4.9 4.9l1.4 1.4M17.7 17.7l1.4 1.4M2 12h2M20 12h2M4.9 19.1l1.4-1.4M17.7 6.3l1.4-1.4"/></svg>
      <svg class="moon" viewBox="0 0 24 24" aria-hidden="true"><path d="M20 14.5A8 8 0 0 1 9.5 4 8 8 0 1 0 20 14.5z"/></svg>
      <span class="lbl" id="thl">โหมดมืด</span>
    </button>
  </span>
</nav>

<main>
<noscript><p style="padding:20px;color:red;text-align:center;">เว็บไซต์นี้จำเป็นต้องเปิดใช้งาน JavaScript เพื่อแสดงสูตรคณิตศาสตร์ KaTeX และสลับหน้าต่างเนื้อหา</p></noscript>
''')

print("Part 1 added.")

# --- 2. SECTION: #sum (สรุปภาพรวม ครบ 11 บท) ---
parts.append(r'''
<section id="sum" class="on">
  <header class="top">
    <p class="kick">แนวทางการเตรียมสอบปฏิบัติการกลศาสตร์ของไหลสำหรับวิศวกรโยธา</p>
    <h1>CE 272 ปฏิบัติการกลศาสตร์ของไหล</h1>
    <p class="sub">สรุปเนื้อหา · สูตรคำนวณ · ขั้นตอนการทดลอง · จุดดักคะแนน ครบทั้ง 11 บท</p>
    <p class="by">ภาควิชาวิศวกรรมโยธา คณะวิศวกรรมศาสตร์ มหาวิทยาลัยธรรมศาสตร์<br>คู่มือฉบับเข้าใจง่าย ปูพื้นฐานจาก First Principles และการพิสูจน์จริง</p>
    <p class="pracnote">โหมดฝึกเปิดอยู่: ซ่อนวิธีทำไว้ แตะแต่ละขั้นเพื่อดู (ลองเขียนเองก่อน) กดปุ่ม "ฝึก" อีกครั้งเพื่อปิด</p>
  </header>

  <h2 class="prob"><span class="tag">ภาพรวม</span>สรุปมโนทัศน์สำคัญและการสอบปฏิบัติการ</h2>
  <div class="stmt">
    <p>คู่มือนี้สรุปเนื้อหาปฏิบัติการกลศาสตร์ของไหล (CE 272) ครบทั้ง 11 บทตามคู่มือแล็บฉบับเต็มของภาควิชา พร้อมเจาะลึกจุดประสงค์ สมการควบคุม การหักล้างของแรงทางฟิสิกส์ การบันทึกข้อมูล และจุดหลอกที่ข้อสอบชอบดักคะแนน เพื่อให้นักศึกษาสามารถทบทวนและซ้อมทำโจทย์ได้อย่างรวดเร็วและแม่นยำ</p>
  </div>

  <div class="jump">
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
      <caption>ตารางสรุปสมการและแก่นการทดลอง ครบ 11 บท</caption>
      <thead>
        <tr>
          <th>บทที่</th>
          <th>ชื่อการทดลอง</th>
          <th>สมการสำคัญ</th>
          <th>ตัวแปรหลักที่ต้องหา</th>
          <th>เครื่องมือสำคัญ</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td><b>1</b></td>
          <td>โต๊ะชลศาสตร์ (Hydraulic Bench)</td>
          <td>\(Q = \frac{\Delta V}{\Delta t}\)</td>
          <td>อัตราการไหลจริง \(Q_{\text{act}}\)</td>
          <td>ถังตวง Volumetric, นาฬิกาจับเวลา, Sight Glass</td>
        </tr>
        <tr>
          <td><b>2</b></td>
          <td>จุดศูนย์กลางแรงดัน (Center of Pressure)</td>
          <td>\(F = \gamma h_{cg} A,\quad y_{cp} = y_c + \frac{I_{xx}}{y_c A}\)</td>
          <td>แรงดัน \(F\), จุดศูนย์กลางแรงดัน \(y_{cp}\)</td>
          <td>ทุ่นเสี้ยววงกลม Quadrant, คานถ่วงสมดุล</td>
        </tr>
        <tr>
          <td><b>3</b></td>
          <td>แรงกระแทกลำน้ำ (Impact of Jet)</td>
          <td>\(F = \rho Q v (\cos\theta + 1)\)</td>
          <td>แรงกระแทก \(F\), โมเมนตัมลำน้ำ</td>
          <td>แผ่นเป้า 90° แบน vs ถ้วย 180° ครึ่งวงกลม</td>
        </tr>
        <tr>
          <td><b>4</b></td>
          <td>สมการเบอร์นูลี่ (Bernoulli &amp; Venturi)</td>
          <td>\(\frac{P_1}{\gamma} + \frac{v_1^2}{2g} + z_1 = \frac{P_2}{\gamma} + \frac{v_2^2}{2g} + z_2\)</td>
          <td>\(Q_{\text{th}}, Q_{\text{act}}, C_d\), เส้น EGL/HGL</td>
          <td>หลอดเวนจูรี่, มาโนมิเตอร์หลายหลอด</td>
        </tr>
        <tr>
          <td><b>5</b></td>
          <td>สมการแมนนิ่ง (Manning's Flow)</td>
          <td>\(V = \frac{1}{n} R_h^{2/3} S_0^{1/2},\quad Q = VA\)</td>
          <td>ความขรุขระ \(n\), รัศมีชลศาสตร์ \(R_h\)</td>
          <td>รางน้ำเปิดปรับเอียง, แผ่นหญ้าเทียมขรุขระ</td>
        </tr>
        <tr>
          <td><b>6</b></td>
          <td>การวัดด้วยฝาย (Weir Flow)</td>
          <td>สี่เหลี่ยม: \(Q \propto H^{1.5}\) · สามเหลี่ยม: \(Q \propto H^{2.5}\)</td>
          <td>\(Q_{\text{th}}, C_d\), กราฟล็อก</td>
          <td>ฝายสันคม, Hook Gauge วัดระดับน้ำ</td>
        </tr>
        <tr>
          <td><b>7</b></td>
          <td>การสูญเสียในท่อ (Pipe Losses)</td>
          <td>\(h_f = f\frac{L}{D}\frac{v^2}{2g},\quad h_m = K\frac{v^2}{2g}\)</td>
          <td>Friction \(f\), เฮดสูญเสียแบบขนาน/อนุกรม</td>
          <td>แผงโครงข่ายท่อ A, B, C, D</td>
        </tr>
        <tr>
          <td><b>8</b></td>
          <td>การไหลผ่านรูลอด (Orifice &amp; Jet)</td>
          <td>\(v_{\text{th}} = \sqrt{2gH},\quad x = 2 C_v \sqrt{yH}\)</td>
          <td>\(C_v, C_c, C_d\), แนววิถีลำน้ำ</td>
          <td>ถังน้ำระดับคงที่, แผงเข็มวัดพิกัดลำน้ำ</td>
        </tr>
        <tr>
          <td><b>9</b></td>
          <td>ทดสอบปั๊มน้ำ (Pump Test)</td>
          <td>\(H = (h_2 - h_1) + H_d,\quad W_i = \gamma Q H\)</td>
          <td>Total Head \(H\), กำลังน้ำ \(W_i\), ประสิทธิภาพ \(\eta_o\)</td>
          <td>ปั๊มเดี่ยว/อนุกรม/ขนาน, เกจความดัน</td>
        </tr>
        <tr>
          <td><b>10</b></td>
          <td>ไหลลอดประตูน้ำ (Sluice Gate)</td>
          <td>\(E = y + \frac{v^2}{2g},\quad Q = C_d y_g B \sqrt{2g y_0}\)</td>
          <td>พลังงานจำเพาะ \(E\), Froude Number \(Fr\)</td>
          <td>บานประตูน้ำตรง, Current meter วัดความเร็ว</td>
        </tr>
        <tr>
          <td><b>11</b></td>
          <td>รางเวนจูรี่ (Venturi Flume)</td>
          <td>Free flow: \(Q = (\frac{2}{3})^{1.5} \sqrt{g} b y_1^{1.5}\)</td>
          <td>Critical depth \(y_c\), Free vs Submerged</td>
          <td>รางน้ำบีบหน้าตัดคอคอดในทางน้ำเปิด</td>
        </tr>
      </tbody>
    </table>
  </div>

  <h3 class="grp" id="sum-b">ข. จุดดักคะแนนและข้อควรระวังในห้องสอบ (Critical Exam Traps)</h3>
  <div class="bx trap">
    <b>กับดักหน่วยยกกำลังสิบ (The 10^X Unit Trap):</b>
    <div>
      ในข้อสอบอาจารย์มักให้ปริมาตรน้ำเป็น <b>ลิตร (L)</b> หรือ <b>มิลลิลิตร (mL)</b> และเวลาเป็น <b>วินาที (s)</b> หรือ <b>นาที (min)</b><br>
      • ห้ามนำค่าลิตรไปคูณกับความเร่งโน้มถ่วงหรือความหนาแน่นตรงๆ เด็ดขาด!<br>
      • กฎเหล็ก: แปลงเป็นหน่วย SI เสมอ: \(1\text{ L} = 10^{-3}\text{ m}^3\), \(1\text{ mL} = 10^{-6}\text{ m}^3\)<br>
      • เช่น \(Q = 12\text{ L/min} \Rightarrow Q = \frac{12 \times 10^{-3}}{60} = 2.0 \times 10^{-4}\text{ m}^3/\text{s}\)
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

  <div class="bx chk">
    <b>การตรวจสอบสภาวะทางฟิสิกส์ (Physical Reality Checks):</b>
    <div>
      • ค่าสัมประสิทธิ์การไหล \(C_d\), \(C_v\), \(C_c\) ต้องน้อยกว่า 1.0 เสมอ (ปกติ \(C_d \approx 0.60 - 0.98\)) ถ้าคำนวณได้เกิน 1 แสดงว่าสลับเศษส่วนหรือลืมแปลงหน่วย<br>
      • แรงกระแทกบนถ้วยครึ่งวงกลม (\(180^\circ\)) ต้องเป็น <b>2 เท่า</b> ของแผ่นเรียบแบนเสมอ (\(F_{\text{hemi}} = 2 F_{\text{flat}}\)) เพราะโมเมนตัมสะท้อนกลับทิศ \(180^\circ\)
    </div>
  </div>

  <div class="pn">
    <span></span>
    <a href="#lab1">บทที่ 1 โต๊ะชลศาสตร์ →</a>
  </div>
</section>
''')

print("Part 2 (Section sum) added successfully.")
