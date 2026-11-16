/* CE 272: Universal Fluid Mechanics Laboratory Calculator */
(function () {
  "use strict";
  var G = 9.81;
  var RHO = 1000.0;
  var GAMMA = 9810.0;

  var form = document.getElementById("calcform");
  if (!form) return;
  var out = document.getElementById("calcout");

  function fmt(x, d) {
    if (x === null || x === undefined || isNaN(x)) return "-";
    var n = Number(x);
    if (Math.abs(n) >= 1e5 || (Math.abs(n) < 1e-3 && Math.abs(n) > 0)) {
      return n.toExponential(d || 3);
    }
    return n.toPrecision(d || 4).replace(/(\.\d*?)0+$/, "$1").replace(/\.$/, "");
  }

  function val(name) {
    var el = form.elements[name];
    if (!el) return NaN;
    var v = parseFloat(el.value);
    return isNaN(v) ? 0 : v;
  }

  function colebrook(re, rr) {
    if (re < 2000) return 64 / re;
    var f = 0.02;
    for (var i = 0; i < 200; i++) {
      var n = Math.pow(-2 * Math.log10(rr / 3.7 + 2.51 / (re * Math.sqrt(f))), -2);
      if (Math.abs(n - f) < 1e-9) return n;
      f = n;
    }
    return f;
  }

  function table(head, rows) {
    var h = "<tr>" + head.map(function (c) { return "<th>" + c + "</th>"; }).join("") + "</tr>";
    var b = rows.map(function (r) {
      return "<tr>" + r.map(function (c) { return "<td>" + c + "</td>"; }).join("") + "</tr>";
    }).join("");
    return '<div class="tw"><table><thead>' + h + "</thead><tbody>" + b + "</tbody></table></div>";
  }

  function solve() {
    var mode = form.elements.mode.value;
    var resHtml = "", tableHead = ["พารามิเตอร์", "ค่าที่คำนวณได้", "หน่วย / คำอธิบาย"], tableRows = [];

    try {
      if (mode === "bench") {
        var vVal = val("b_vol"), vUnit = form.elements.b_vol_unit.value;
        var tVal = val("b_time");
        if (vVal <= 0 || tVal <= 0) throw new Error("กรุณากรอกปริมาตรและเวลาเป็นตัวเลขบวก");
        var vM3 = (vUnit === "L") ? vVal * 1e-3 : (vUnit === "mL") ? vVal * 1e-6 : vVal;
        var qM3s = vM3 / tVal;
        var qLs = qM3s * 1e3;
        var qLmin = qLs * 60;
        resHtml = "Q = " + fmt(qM3s, 4) + " m³/s  (" + fmt(qLs, 3) + " L/s, " + fmt(qLmin, 3) + " L/min)";
        tableRows = [
          ["ปริมาตรน้ำ (Volume)", fmt(vVal, 4), vUnit + " = " + fmt(vM3, 4) + " m³"],
          ["เวลาในการเก็บน้ำ (Time)", fmt(tVal, 3), "s"],
          ["อัตราการไหลจริง (Q_actual)", fmt(qM3s, 4), "m³/s  [SI Unit]"],
          ["อัตราการไหล (ลิตรต่อวินาที)", fmt(qLs, 3), "L/s"],
          ["อัตราการไหล (ลิตรต่อนาที)", fmt(qLmin, 3), "L/min"]
        ];
      } else if (mode === "cp") {
        var d = val("cp_d") / 100.0; // cm -> m
        var D = (val("cp_D") || 10.0) / 100.0;
        var B = (val("cp_B") || 7.5) / 100.0;
        var L = (val("cp_L") || 28.0) / 100.0;
        var H = (val("cp_H") || 20.0) / 100.0;
        var mGram = val("cp_m");
        if (d <= 0) throw new Error("กรุณากรอกระดับน้ำ d เป็นค่าบวก");

        var isPartial = (d < D);
        var F_th, ycp_th, h_double_prime = 0, ycp_exp = null;
        if (isPartial) {
          F_th = 0.5 * RHO * G * B * d * d;
          ycp_th = (2.0 / 3.0) * d;
        } else {
          F_th = RHO * G * B * D * (d - D / 2.0);
          var yc = d - D / 2.0;
          ycp_th = yc + (D * D) / (12.0 * yc);
        }

        if (mGram > 0) {
          var massKg = mGram / 1000.0;
          h_double_prime = (massKg * L) / (isPartial ? (0.5 * RHO * B * d * d) : (RHO * B * D * (d - D / 2.0)));
          ycp_exp = h_double_prime - (H - d);
        }

        resHtml = (isPartial ? "[จมบางส่วน d < D] " : "[จมมิดทั้งหมด d ≥ D] ") +
          "F_th = " + fmt(F_th, 4) + " N,  y_cp(ทฤษฎี) = " + fmt(ycp_th * 100, 3) + " cm";
        if (ycp_exp !== null) resHtml += ",  y_cp(ทดลอง) = " + fmt(ycp_exp * 100, 3) + " cm";

        tableRows = [
          ["สภาวะการจม", isPartial ? "จมบางส่วน (d < D)" : "จมมิดทั้งหมด (d ≥ D)", "D = " + fmt(D * 100, 1) + " cm, d = " + fmt(d * 100, 1) + " cm"],
          ["แรงดันน้ำตามทฤษฎี (F_th)", fmt(F_th, 4), "N  (นิวตัน)"],
          ["จุดศูนย์กลางแรงดันทางทฤษฎี (y_cp,th)", fmt(ycp_th * 100, 4), "cm จากผิวน้ำ"],
          ["ระยะแขนโมเมนต์คาน (h'')", mGram > 0 ? fmt(h_double_prime * 100, 4) : "-", "cm จากจุดหมุนถึงแนวแรง"],
          ["จุดศูนย์กลางแรงดันจากการทดลอง (y_cp,exp)", ycp_exp !== null ? fmt(ycp_exp * 100, 4) : "-", "cm  [h'' - (H - d)]"]
        ];
      } else if (mode === "jet") {
        var jetQ = val("jet_q") * 1e-3; // L/s -> m3/s
        var jetD = (val("jet_d") || 8.0) * 1e-3; // mm -> m
        var targetType = form.elements.jet_target.value;
        var thetaDeg = parseFloat(targetType);
        if (isNaN(thetaDeg)) thetaDeg = val("jet_custom_theta");

        if (jetQ <= 0 || jetD <= 0) throw new Error("กรุณากรอกอัตราการไหลและขนาดหัวฉีดเป็นค่าบวก");
        var jetArea = (Math.PI * jetD * jetD) / 4.0;
        var jetV = jetQ / jetArea;
        var thetaRad = (thetaDeg * Math.PI) / 180.0;
        var jetF = RHO * jetQ * jetV * (Math.cos(thetaRad) + 1.0);
        var jetM = (jetF / G) * 1000.0; // g

        resHtml = "แรงกระแทก F = " + fmt(jetF, 4) + " N  (เทียบเท่าตุ้มน้ำหนัก " + fmt(jetM, 3) + " g)";
        tableRows = [
          ["ชนิดของฉากกั้น (Vane)", thetaDeg === 90 ? "แผ่นเรียบแบน 90°" : (thetaDeg === 0 ? "ถ้วยครึ่งวงกลม 180° (θ=0°)" : "มุม " + thetaDeg + "°"), "cos(θ)+1 = " + fmt(Math.cos(thetaRad) + 1, 3)],
          ["ความเร็วลำน้ำที่หัวฉีด (v)", fmt(jetV, 4), "m/s  (Nozzle D = " + fmt(jetD * 1000, 1) + " mm)"],
          ["แรงกระแทกตามโมเมนตัม (F)", fmt(jetF, 4), "N  [F = ρ Q v (cos θ + 1)]"],
          ["มวลตุ้มน้ำหนักที่ถ่วงสมดุล (m)", fmt(jetM, 3), "g  (กรัม)"]
        ];
      } else if (mode === "venturi") {
        var D1 = val("v_d1") * 1e-2, D2 = val("v_d2") * 1e-2; // cm -> m
        var dh = val("v_dh") * 1e-2; // cm water -> m
        var qActInput = val("v_qact") * 1e-3; // L/s -> m3/s
        if (D1 <= 0 || D2 <= 0 || dh <= 0) throw new Error("กรุณากรอกขนาดท่อและผลต่างระดับน้ำ h1 - h2 เป็นค่าบวก");
        var A1 = (Math.PI * D1 * D1) / 4.0, A2 = (Math.PI * D2 * D2) / 4.0;
        var ratio = A1 / A2;
        var v1_th = Math.sqrt((2.0 * G * dh) / (ratio * ratio - 1.0));
        var q_th = A1 * v1_th;
        var cd = (qActInput > 0) ? (qActInput / q_th) : null;

        resHtml = "Q_th = " + fmt(q_th * 1e3, 4) + " L/s (" + fmt(q_th, 4) + " m³/s)";
        if (cd !== null) resHtml += ",  C_d = " + fmt(cd, 3);
        tableRows = [
          ["อัตราส่วนพื้นที่หน้าตัด (A1/A2)", fmt(ratio, 3), "A1 = " + fmt(A1 * 1e4, 2) + " cm², A2 = " + fmt(A2 * 1e4, 2) + " cm²"],
          ["ผลต่างความดัน (h1 - h2)", fmt(dh * 100, 2), "cm ของน้ำ (" + fmt(dh, 4) + " m)"],
          ["ความเร็วทฤษฎีที่ทางเข้า (v1)", fmt(v1_th, 3), "m/s"],
          ["อัตราการไหลทางทฤษฎี (Q_th)", fmt(q_th, 4), "m³/s  (" + fmt(q_th * 1e3, 4) + " L/s)"],
          ["สัมประสิทธิ์การปรับแก้ (C_d)", cd !== null ? fmt(cd, 4) : "-", cd !== null ? "Q_act / Q_th" : "กรอก Q_act เพื่อคำนวณ"]
        ];
      } else if (mode === "manning") {
        var mB = val("m_b"), mY = val("m_y");
        var mS = val("m_s");
        var mN = val("m_n") || 0.012;
        if (mB <= 0 || mY <= 0 || mS <= 0 || mN <= 0) throw new Error("กรุณากรอกความกว้าง ความลึก ความชัน และค่า n เป็นค่าบวก");
        var mA = mB * mY;
        var mP = mB + 2.0 * mY;
        var mR = mA / mP;
        var mV = (1.0 / mN) * Math.pow(mR, 2.0 / 3.0) * Math.sqrt(mS);
        var mQ = mV * mA;

        resHtml = "V = " + fmt(mV, 3) + " m/s,  Q = " + fmt(mQ, 4) + " m³/s (" + fmt(mQ * 3600, 3) + " m³/hr)";
        tableRows = [
          ["พื้นที่หน้าตัดการไหล (A)", fmt(mA, 4), "m²  [B × y]"],
          ["เส้นขอบเปียก (P_w)", fmt(mP, 4), "m  [B + 2y ไม่รวมผิวบน]"],
          ["รัศมีชลศาสตร์ (R_h)", fmt(mR, 4), "m  [A / P_w]"],
          ["ความเร็วเฉลี่ย (V)", fmt(mV, 4), "m/s  [(1/n) R^(2/3) S^(1/2)]"],
          ["อัตราการไหล (Q)", fmt(mQ, 4), "m³/s  (" + fmt(mQ * 3600, 3) + " m³/hr)"]
        ];
      } else if (mode === "weir") {
        var wType = form.elements.w_type.value;
        var wH = val("w_h") * 1e-2; // cm -> m
        var wB = val("w_b") * 1e-2; // cm -> m
        var wCd = val("w_cd") || 0.62;
        if (wH <= 0) throw new Error("กรุณากรอกระดับน้ำเหนือสันฝาย H เป็นค่าบวก");
        var wQth, wQact;
        if (wType === "rect") {
          if (wB <= 0) throw new Error("ฝายสี่เหลี่ยมต้องกรอกความกว้าง B");
          wQth = (2.0 / 3.0) * wB * Math.sqrt(2 * G) * Math.pow(wH, 1.5);
          wQact = wCd * wQth;
          resHtml = "[ฝายสี่เหลี่ยม] Q_th = " + fmt(wQth * 1e3, 3) + " L/s,  Q_act = " + fmt(wQact * 1e3, 3) + " L/s";
        } else {
          wQth = (8.0 / 15.0) * Math.sqrt(2 * G) * Math.pow(wH, 2.5); // theta = 90 deg, tan(45)=1
          wQact = wCd * wQth;
          resHtml = "[ฝาย 90° V-Notch] Q_th = " + fmt(wQth * 1e3, 3) + " L/s,  Q_act = " + fmt(wQact * 1e3, 3) + " L/s";
        }
        tableRows = [
          ["ชนิดของฝาย", wType === "rect" ? "ฝายสี่เหลี่ยมสันคม (Rectangular)" : "ฝายสามเหลี่ยม 90° (V-Notch)", "H = " + fmt(wH * 100, 2) + " cm"],
          ["อัตราการไหลทางทฤษฎี (Q_th)", fmt(wQth, 4), "m³/s  (" + fmt(wQth * 1e3, 3) + " L/s)"],
          ["สัมประสิทธิ์การไหล (C_d)", fmt(wCd, 3), "-"],
          ["อัตราการไหลจริง (Q_act)", fmt(wQact, 4), "m³/s  (" + fmt(wQact * 1e3, 3) + " L/s)"]
        ];
      } else if (mode === "pump") {
        var pConfig = form.elements.p_config.value;
        var pQ = val("p_q") * 1e-3; // L/s -> m3/s
        var ph1 = val("p_h1"); // m
        var ph2 = val("p_h2"); // m
        var pWm = val("p_wm"); // Watts
        var pHd = (pConfig === "single") ? 0.15 : (pConfig === "series") ? -0.07 : 0.94;
        var pInlet = (pConfig === "series") ? 0.0 : ph1;
        var pTotalH = (ph2 - pInlet) + pHd;
        var pWi = (pQ > 0 && pTotalH > 0) ? (GAMMA * pQ * pTotalH) : 0;
        var pEff = (pWm > 0 && pWi > 0) ? (pWi / pWm) * 100.0 : null;

        resHtml = "Total Head H = " + fmt(pTotalH, 3) + " m,  Water Power Wi = " + fmt(pWi, 3) + " Watts";
        if (pEff !== null) resHtml += ",  η_o = " + fmt(pEff, 2) + "%";

        tableRows = [
          ["โหมดการต่อเครื่องสูบน้ำ", pConfig === "single" ? "ปั๊มเดี่ยว (Single)" : (pConfig === "series" ? "ต่ออนุกรม (Series: H เพิ่ม 2 เท่า)" : "ต่อขนาน (Parallel: Q เพิ่ม 2 เท่า)"), "ค่าแก้ระดับ Hd = " + (pHd >= 0 ? "+" : "") + fmt(pHd, 2) + " m"],
          ["เฮดท่อดูด (h1)", pConfig === "series" ? "0.00 (เปิดสู่อากาศ)" : fmt(ph1, 3), "m ของน้ำ"],
          ["เฮดท่อส่ง (h0 / hm)", fmt(ph2, 3), "m ของน้ำ"],
          ["Total Head (H)", fmt(pTotalH, 3), "m  [(h2 - h1) + Hd]"],
          ["กำลังไฮดรอลิกของน้ำ (Wi)", fmt(pWi, 3), "Watts  [γ Q H]"],
          ["ประสิทธิภาพรวม (η_o)", pEff !== null ? fmt(pEff, 2) + " %" : "-", pEff !== null ? "[Wi / Wm × 100]" : "กรอกกำลังมอเตอร์ Wm เพื่อคำนวณ"]
        ];
      } else if (mode === "orifice") {
        var oH = val("o_h"); // m
        var od0 = val("o_d0") * 1e-3; // mm -> m
        var ox = val("o_x"); // m
        var oy = val("o_y"); // m
        var odc = val("o_dc") * 1e-3; // mm -> m
        if (oH <= 0 || ox <= 0 || oy <= 0) throw new Error("กรุณากรอก H, x, y เป็นค่าบวก");

        var ov_th = Math.sqrt(2 * G * oH);
        var oCv = ox / (2.0 * Math.sqrt(oy * oH));
        var ov_act = oCv * ov_th;
        var oCc = (odc > 0 && od0 > 0) ? Math.pow(odc / od0, 2) : null;
        var oCd = (oCc !== null) ? (oCv * oCc) : null;

        resHtml = "Cv = " + fmt(oCv, 4) + ",  v_act = " + fmt(ov_act, 3) + " m/s (v_th = " + fmt(ov_th, 3) + " m/s)";
        if (oCd !== null) resHtml += ",  Cd = " + fmt(oCd, 4);

        tableRows = [
          ["ความเร็วทฤษฎี (v_th)", fmt(ov_th, 3), "m/s  [√(2gH)]"],
          ["สัมประสิทธิ์ความเร็ว (C_v)", fmt(oCv, 4), "จากวิถีลำน้ำ: x / (2√(yH))"],
          ["ความเร็วจริงที่ Vena Contracta", fmt(ov_act, 3), "m/s  [Cv × v_th]"],
          ["สัมประสิทธิ์การหดตัว (C_c)", oCc !== null ? fmt(oCc, 4) : "-", oCc !== null ? "(d_c / d_0)²" : "กรอก d_c เพื่อคำนวณ"],
          ["สัมประสิทธิ์อัตราการไหล (C_d)", oCd !== null ? fmt(oCd, 4) : "-", oCd !== null ? "Cv × Cc" : "-"]
        ];
      } else if (mode === "sluice") {
        var sY0 = val("s_y0"), sYg = val("s_yg"), sY1 = val("s_y1"), sB = val("s_b") || 1.0;
        if (sY0 <= 0 || sY1 <= 0 || sY0 <= sY1) throw new Error("กรุณากรอก y0 และ y1 โดยที่ y0 > y1");
        var sQth = (sB * sY1 * Math.sqrt(2 * G * sY0)) / Math.sqrt(sY1 / sY0 + 1.0);
        var sV0 = sQth / (sB * sY0);
        var sV1 = sQth / (sB * sY1);
        var sFr0 = sV0 / Math.sqrt(G * sY0);
        var sFr1 = sV1 / Math.sqrt(G * sY1);
        var sCc = (sYg > 0) ? (sY1 / sYg) : null;

        resHtml = "Q_th = " + fmt(sQth, 4) + " m³/s,  Fr0 = " + fmt(sFr0, 3) + " (Subcritical),  Fr1 = " + fmt(sFr1, 3) + " (Supercritical)";
        tableRows = [
          ["อัตราการไหลทฤษฎี (Q_th)", fmt(sQth, 4), "m³/s"],
          ["สภาวะเหนือบานน้ำ (Upstream)", "Fr0 = " + fmt(sFr0, 3) + " < 1", "Subcritical (น้ำลึก ไหลช้า)"],
          ["สภาวะใต้บานน้ำ (Downstream)", "Fr1 = " + fmt(sFr1, 3) + " > 1", "Supercritical (น้ำตื้น พุ่งแรง)"],
          ["สัมประสิทธิ์การลดขนาด (C_c)", sCc !== null ? fmt(sCc, 3) : "-", sCc !== null ? "y1 / yg" : "-"]
        ];
      } else if (mode === "flume") {
        var fb = val("f_b"), fy1 = val("f_y1");
        if (fb <= 0 || fy1 <= 0) throw new Error("กรุณากรอกความกว้างคอคอด b และระดับน้ำต้นน้ำ y1 เป็นค่าบวก");
        var fQth = Math.pow(2.0 / 3.0, 1.5) * Math.sqrt(G) * fb * Math.pow(fy1, 1.5);
        var fYc = (2.0 / 3.0) * fy1;
        resHtml = "[Free Flow] Q_th = " + fmt(fQth, 4) + " m³/s (" + fmt(fQth * 1e3, 3) + " L/s),  yc = " + fmt(fYc * 100, 2) + " cm";
        tableRows = [
          ["สภาวะการไหล", "การไหลแบบอิสระ (Free Flow)", "เกิด Critical flow ที่คอคอด (Fr = 1)"],
          ["ความลึกวิกฤตที่คอคอด (y_c)", fmt(fYc * 100, 2), "cm  [2/3 ของ y1]"],
          ["อัตราการไหลทางทฤษฎี (Q_th)", fmt(fQth, 4), "m³/s  (" + fmt(fQth * 1e3, 3) + " L/s)"]
        ];
      }

      out.innerHTML = '<p class="res">' + resHtml + "</p>" + table(tableHead, tableRows);
    } catch (e) {
      out.innerHTML = '<p class="err">⚠️ ข้อผิดพลาด: ' + e.message + "</p>";
    }
  }

  function updateModeFields() {
    var mode = form.elements.mode.value;
    [].forEach.call(form.querySelectorAll("[data-m]"), function (el) {
      var modes = el.getAttribute("data-m").split(" ");
      el.hidden = modes.indexOf(mode) < 0;
    });
    out.innerHTML = "";
  }

  form.elements.mode.addEventListener("change", updateModeFields);
  form.addEventListener("submit", function (e) {
    e.preventDefault();
    solve();
  });

  updateModeFields();
})();
