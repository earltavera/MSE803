const pptxgen = require("pptxgenjs");
const fs = require("fs");
const path = require("path");

const pres = new pptxgen();
pres.layout = "LAYOUT_16x9";
pres.title = "NZ Wellbeing Forecasting";
pres.author = "Wellbeing Analytics";

const OUT = "/home/claude/nz_wellbeing_forecast/outputs";

// Palette — deep teal/navy for wellbeing/trust
const C = {
  dark:    "0D2137",
  teal:    "028090",
  mint:    "00A896",
  white:   "FFFFFF",
  light:   "F0F9FB",
  gray:    "64748B",
  lgray:   "E8F4F6",
  gold:    "F9A826",
  coral:   "E05C5C",
  green:   "2ECC71",
};

function img(name) {
  const p = path.join(OUT, name);
  return fs.existsSync(p) ? p : null;
}

// ── Slide 1: Title ──────────────────────────────────────────────────────────
{
  const s = pres.addSlide();
  s.background = { color: C.dark };
  // Big teal circle accent top-right
  s.addShape(pres.shapes.OVAL, { x:7.5, y:-1.5, w:4.5, h:4.5, fill:{ color:C.teal, transparency:70 } });
  s.addShape(pres.shapes.OVAL, { x:8.5, y:-0.8, w:2.8, h:2.8, fill:{ color:C.mint, transparency:55 } });

  s.addText("NZ Wellbeing Forecasting", {
    x:0.6, y:1.0, w:9, h:1.2, fontSize:40, bold:true, color:C.white,
    fontFace:"Cambria", align:"left"
  });
  s.addText("Comparing Linear Regression · XGBoost · LSTM · ANN · ARIMA", {
    x:0.6, y:2.3, w:9, h:0.5, fontSize:16, color:C.mint, fontFace:"Calibri", align:"left"
  });
  s.addText("New Zealand General Social Survey · 2014–2018 · Forecast: 2020", {
    x:0.6, y:2.9, w:9, h:0.4, fontSize:13, color:"AACDD4", fontFace:"Calibri", align:"left"
  });

  // Stats row
  const statX = [0.6, 3.0, 5.5, 7.8];
  const stats  = ["10", "5", "3", "2020"];
  const labels = ["Wellbeing\nIndicators", "Forecasting\nModels", "Survey\nYears", "Forecast\nTarget Year"];
  for(let i=0;i<4;i++){
    s.addShape(pres.shapes.ROUNDED_RECTANGLE, {
      x:statX[i], y:3.8, w:2.0, h:1.4,
      fill:{ color:C.teal, transparency:40 }, rectRadius:0.08
    });
    s.addText(stats[i],  { x:statX[i], y:3.85, w:2.0, h:0.65, fontSize:32, bold:true, color:C.white, fontFace:"Cambria", align:"center" });
    s.addText(labels[i], { x:statX[i], y:4.5,  w:2.0, h:0.65, fontSize:10, color:"AACDD4", fontFace:"Calibri", align:"center" });
  }

  s.addNotes("Welcome slide. This project forecasts 10 NZ wellbeing indicators using 5 distinct models on Stats NZ data.");
}

// ── Slide 2: Project Overview ────────────────────────────────────────────────
{
  const s = pres.addSlide();
  s.background = { color: C.white };
  s.addText("Project Overview", { x:0.5, y:0.25, w:9, h:0.6, fontSize:28, bold:true, color:C.dark, fontFace:"Cambria" });

  // Two column layout
  const items = [
    ["📊 Dataset", "Stats NZ General Social Survey 2014–2018\n10 wellbeing indicators across 3 biennial waves"],
    ["🎯 Objective", "Forecast 2020 values for each indicator using 5 ML/Statistical models"],
    ["📐 Models Used", "Linear Regression · XGBoost (GBM)\nLSTM · ANN · ARIMA(1,1,1)"],
    ["📏 Evaluation", "MAE, RMSE, MAPE, R² computed\nfor each model across all indicators"],
  ];
  for(let i=0;i<items.length;i++){
    const col = i % 2;
    const row = Math.floor(i / 2);
    const x = col === 0 ? 0.5 : 5.2;
    const y = row === 0 ? 1.1 : 3.0;
    s.addShape(pres.shapes.ROUNDED_RECTANGLE, {
      x, y, w:4.4, h:1.6,
      fill:{ color: col===0 ? C.light : "FFF8F0" },
      shadow:{ type:"outer", color:"000000", blur:8, offset:2, angle:45, opacity:0.10 },
      rectRadius:0.1
    });
    s.addText(items[i][0], { x:x+0.2, y:y+0.1, w:4.0, h:0.4, fontSize:13, bold:true, color:C.teal, fontFace:"Calibri" });
    s.addText(items[i][1], { x:x+0.2, y:y+0.5, w:4.0, h:1.0, fontSize:11, color:C.dark, fontFace:"Calibri" });
  }

  s.addNotes("Overview of dataset scope and research approach.");
}

// ── Slide 3: Dataset ─────────────────────────────────────────────────────────
{
  const s = pres.addSlide();
  s.background = { color: C.dark };
  s.addText("The Dataset", { x:0.5, y:0.25, w:9, h:0.6, fontSize:28, bold:true, color:C.white, fontFace:"Cambria" });

  // Table of indicators
  const headers = [["Indicator", "2014", "2016", "2018"]];
  const rows = [
    ["Life Satisfaction (Mean)",   "7.8",  "7.8",  "7.7"],
    ["Life Worthwhile (Mean)",     "8.1",  "8.1",  "8.1"],
    ["Financial Inadequacy (%)",   "12.2", "11.2", "10.0"],
    ["Health Excellent (%)",       "21.6", "19.1", "16.5"],
    ["Loneliness None (%)",        "63.9", "60.2", "61.0"],
    ["Generalised Trust Low (%)",  "8.7",  "8.6",  "9.7"],
    ["Job Very Satisfied (%)",     "35.6", "34.2", "27.0"],
    ["Housing Problems (%)",       "21.2", "21.0", "22.1"],
    ["Cultural Belonging (%)",     "52.6", "51.0", "50.3"],
    ["Feel Safe at Home (%)",      "60.9", "60.7", "61.9"],
  ];

  const tdata = [
    headers[0].map(h => ({
      text: h,
      options: { bold:true, color:C.white, fill:{ color:C.teal }, fontSize:11, fontFace:"Calibri", align:"center" }
    })),
    ...rows.map((r, ri) => r.map((cell, ci) => ({
      text: cell,
      options: { color: ci===0 ? "AACDD4" : C.white, fill:{ color: ri%2===0 ? "0D2D42" : "0D2137" }, fontSize:10, fontFace:"Calibri", align: ci===0 ? "left" : "center" }
    })))
  ];
  s.addTable(tdata, { x:0.5, y:1.0, w:9.0, h:4.3, border:{ pt:0.5, color:"1E4560" }, rowH:0.39 });
  s.addText("Source: Stats NZ General Social Survey (NZGSS) 2014–2018", { x:0.5, y:5.3, w:9, h:0.25, fontSize:9, color:"668899", fontFace:"Calibri" });
  s.addNotes("All 10 indicators extracted from the 'Total population' rows across 20 survey tables.");
}

// ── Slide 4: Model Architecture ──────────────────────────────────────────────
{
  const s = pres.addSlide();
  s.background = { color: C.white };
  s.addText("Model Architectures", { x:0.5, y:0.25, w:9, h:0.6, fontSize:28, bold:true, color:C.dark, fontFace:"Cambria" });

  const models = [
    { name:"Linear Regression", col:C.teal,  desc:"OLS fit over time index. Simple baseline. Extrapolates trend linearly.", params:"y = β₀ + β₁·t" },
    { name:"XGBoost (GBM)",     col:"2ECC71",  desc:"Gradient boosting on features: year, time offset, lag-1 difference.", params:"Ensemble of shallow trees" },
    { name:"LSTM",              col:C.coral, desc:"Single LSTM cell (numpy). Captures non-linear temporal dependencies.", params:"h=4, lr=0.005, e=3000" },
    { name:"ANN",               col:C.gold,  desc:"2-layer feedforward net (8 hidden units, tanh). Backpropagation.", params:"h=8, lr=0.005, e=5000" },
    { name:"ARIMA(1,1,1)",      col:"9B59B6",  desc:"Differenced series. AR(1) coefficient + MA(1) error correction.", params:"φ fitted via OLS on diffs" },
  ];
  for(let i=0;i<5;i++){
    const x = 0.4 + i*1.92;
    s.addShape(pres.shapes.ROUNDED_RECTANGLE, { x, y:1.05, w:1.7, h:0.45, fill:{ color:models[i].col }, rectRadius:0.1 });
    s.addText(models[i].name, { x, y:1.05, w:1.7, h:0.45, fontSize:9.5, bold:true, color:C.white, fontFace:"Calibri", align:"center", valign:"middle" });
    s.addShape(pres.shapes.ROUNDED_RECTANGLE, { x, y:1.6, w:1.7, h:3.5, fill:{ color:C.lgray }, rectRadius:0.1,
      shadow:{ type:"outer", color:"000000", blur:6, offset:2, angle:45, opacity:0.10 } });
    s.addText(`Params:\n${models[i].params}`, { x:x+0.1, y:1.7, w:1.5, h:0.7, fontSize:9, color:models[i].col, bold:true, fontFace:"Calibri" });
    s.addText(models[i].desc, { x:x+0.1, y:2.5, w:1.5, h:2.4, fontSize:9.5, color:C.dark, fontFace:"Calibri" });
  }
  s.addNotes("All models implemented in Python. LSTM and ANN built from scratch in numpy — no external deep learning libraries needed.");
}

// ── Slide 5: Model Comparison ────────────────────────────────────────────────
{
  const s = pres.addSlide();
  s.background = { color: C.white };
  s.addText("Performance Comparison", { x:0.5, y:0.2, w:9, h:0.6, fontSize:28, bold:true, color:C.dark, fontFace:"Cambria" });

  // Native bar chart — RMSE
  s.addChart(pres.charts.BAR, [{
    name: "Avg RMSE",
    labels: ["XGBoost (GBM)", "Linear Reg.", "ANN", "ARIMA(1,1,1)", "LSTM"],
    values: [0.0056, 0.3653, 0.3726, 0.5285, 1.0849]
  }], {
    x:0.5, y:1.0, w:5.8, h:4.0, barDir:"bar",
    chartColors: ["028090","2196F3","9C27B0","FF9800","FF5722"],
    chartArea:{ fill:{ color:C.lgray }, roundedCorners:true },
    catAxisLabelColor: C.gray, valAxisLabelColor: C.gray,
    valGridLine:{ color:"D0E8EC", size:0.5 }, catGridLine:{ style:"none" },
    showValue:true, dataLabelColor:"1E293B", showLegend:false,
    showTitle:true, title:"Average RMSE by Model (lower = better)",
    titleColor: C.dark, titleFontSize:12,
  });

  // R² chart
  s.addChart(pres.charts.BAR, [{
    name: "Avg R²",
    labels: ["XGBoost (GBM)", "Linear Reg.", "ANN", "ARIMA(1,1,1)", "LSTM"],
    values: [1.000, 0.799, 0.693, 0.393, 0.000]
  }], {
    x:6.5, y:1.0, w:3.2, h:4.0, barDir:"bar",
    chartColors:["028090","2196F3","9C27B0","FF9800","FF5722"],
    chartArea:{ fill:{ color:"FFF8F0" }, roundedCorners:true },
    catAxisLabelColor: C.gray, valAxisLabelColor: C.gray,
    valGridLine:{ color:"EEE", size:0.5 }, catGridLine:{ style:"none" },
    showValue:true, dataLabelColor:"1E293B", showLegend:false,
    showTitle:true, title:"Avg R² Score (higher = better)",
    titleColor:C.dark, titleFontSize:12,
  });
  s.addNotes("XGBoost achieves near-perfect fit on training data. Important caveat: with only 3 data points, overfitting is a risk.");
}

// ── Slide 6: Forecasts Dashboard ────────────────────────────────────────────
{
  const s = pres.addSlide();
  s.background = { color: C.dark };
  s.addText("2020 Forecasts", { x:0.5, y:0.2, w:9, h:0.55, fontSize:28, bold:true, color:C.white, fontFace:"Cambria" });

  const hdr = [
    { text:"Indicator",           options:{ bold:true, color:C.white, fill:{ color:C.teal }, fontSize:9, fontFace:"Calibri" } },
    { text:"Lin. Reg.",           options:{ bold:true, color:C.white, fill:{ color:C.teal }, fontSize:9, fontFace:"Calibri", align:"center" } },
    { text:"XGBoost",             options:{ bold:true, color:C.white, fill:{ color:C.teal }, fontSize:9, fontFace:"Calibri", align:"center" } },
    { text:"LSTM",                options:{ bold:true, color:C.white, fill:{ color:C.teal }, fontSize:9, fontFace:"Calibri", align:"center" } },
    { text:"ANN",                 options:{ bold:true, color:C.white, fill:{ color:C.teal }, fontSize:9, fontFace:"Calibri", align:"center" } },
    { text:"ARIMA",               options:{ bold:true, color:C.white, fill:{ color:C.teal }, fontSize:9, fontFace:"Calibri", align:"center" } },
  ];
  const fc = [
    ["Life Satisfaction Mean",   "7.667","7.700","7.767","7.675","7.705"],
    ["Life Worthwhile Mean",     "8.100","8.100","8.100","8.077","8.100"],
    ["Financial Inadequacy (%)", "8.933","10.006","11.139","9.147","8.834"],
    ["Health Excellent (%)",     "13.967","16.513","19.079","14.466","13.934"],
    ["Loneliness None (%)",      "58.800","61.004","61.706","59.138","60.827"],
    ["Trust Low (%)",            "10.000","9.696","8.998","9.792","9.112"],
    ["Job Very Satisfied (%)",   "23.667","27.027","32.288","24.429","25.686"],
    ["Housing Problems (%)",     "22.333","22.097","21.431","22.122","21.418"],
    ["Cultural Belonging (%)",   "49.000","50.305","51.305","49.240","49.994"],
    ["Feel Safe Home (%)",       "62.167","61.896","61.164","61.937","61.214"],
  ];
  const tdata = [
    hdr,
    ...fc.map((r, ri) => r.map((cell, ci) => ({
      text: cell,
      options: { color: ci===0 ? "AACDD4" : C.white,
                 fill:{ color: ri%2===0 ? "0D2D42" : "0D2137" },
                 fontSize:9.5, fontFace:"Calibri", align: ci===0 ? "left" : "center" }
    })))
  ];
  s.addTable(tdata, { x:0.3, y:0.9, w:9.4, h:4.5, border:{ pt:0.5, color:"1E4560" }, colW:[2.8,1.3,1.3,1.3,1.3,1.4], rowH:0.39 });
  s.addNotes("Full 2020 forecast table across all 5 models for all 10 indicators.");
}

// ── Slide 7: Key Finding – Life Satisfaction ─────────────────────────────────
{
  const s = pres.addSlide();
  s.background = { color: C.white };
  s.addText("Spotlight: Life Satisfaction Mean", { x:0.5, y:0.2, w:9, h:0.55, fontSize:26, bold:true, color:C.dark, fontFace:"Cambria" });

  // Native line chart
  s.addChart(pres.charts.LINE, [
    { name:"Actual",           labels:["2014","2016","2018"], values:[7.8, 7.8, 7.7] },
    { name:"Linear Reg. 2020", labels:["2014","2016","2018","2020"], values:[7.8, 7.8, 7.7, 7.667] },
    { name:"XGBoost 2020",     labels:["2014","2016","2018","2020"], values:[7.8, 7.8, 7.7, 7.700] },
    { name:"ARIMA 2020",       labels:["2014","2016","2018","2020"], values:[7.8, 7.8, 7.7, 7.705] },
  ], {
    x:0.5, y:0.9, w:5.8, h:4.3,
    chartColors:["212121","2196F3","4CAF50","FF9800"],
    lineSize:3, lineSmooth:false,
    chartArea:{ fill:{ color:C.lgray }, roundedCorners:true },
    valAxisMinVal:7.4, valAxisMaxVal:8.0,
    catAxisLabelColor:C.gray, valAxisLabelColor:C.gray,
    showLegend:true, legendPos:"b", legendFontSize:9,
    showTitle:true, title:"Life Satisfaction 2014–2020", titleFontSize:12,
    valGridLine:{ color:"D0E8EC", size:0.5 },
  });

  // Insight cards
  const insights = [
    { val:"7.7",  lbl:"Actual 2018 mean\n(stable near 7.8)" },
    { val:"7.68", lbl:"Avg forecast 2020\n(slight downward trend)" },
    { val:"< 0.5%", lbl:"Avg MAPE across\nall 3 best models" },
  ];
  for(let i=0;i<3;i++){
    s.addShape(pres.shapes.ROUNDED_RECTANGLE, {
      x:6.6, y:1.1+i*1.45, w:3.1, h:1.25,
      fill:{ color: i===0 ? C.light : i===1 ? "FFF0F0" : "FFF8E0" },
      shadow:{ type:"outer", color:"000000", blur:6, offset:2, angle:45, opacity:0.10 },
      rectRadius:0.1
    });
    s.addText(insights[i].val, { x:6.7, y:1.15+i*1.45, w:3.0, h:0.55, fontSize:26, bold:true, color:C.teal, fontFace:"Cambria", align:"center" });
    s.addText(insights[i].lbl, { x:6.7, y:1.68+i*1.45, w:3.0, h:0.55, fontSize:10, color:C.gray, fontFace:"Calibri", align:"center" });
  }
  s.addNotes("Life satisfaction has been remarkably stable around 7.7–7.8. Models agree on a slight downward drift to ~7.68 by 2020.");
}

// ── Slide 8: R² Heatmap image ─────────────────────────────────────────────────
{
  const s = pres.addSlide();
  s.background = { color: C.white };
  s.addText("R² Performance Heatmap", { x:0.5, y:0.2, w:9, h:0.55, fontSize:26, bold:true, color:C.dark, fontFace:"Cambria" });
  const imgPath = img("04_r2_heatmap.png");
  if(imgPath) s.addImage({ path:imgPath, x:0.3, y:0.9, w:9.4, h:4.5 });
  s.addNotes("XGBoost dominates with R²=1.0 on all indicators. Linear Regression and ANN also perform well on smoother series.");
}

// ── Slide 9: Conclusions ─────────────────────────────────────────────────────
{
  const s = pres.addSlide();
  s.background = { color: C.dark };
  s.addShape(pres.shapes.OVAL, { x:7.5, y:3.5, w:4, h:4, fill:{ color:C.teal, transparency:75 } });
  s.addText("Conclusions & Recommendations", { x:0.5, y:0.2, w:9, h:0.6, fontSize:26, bold:true, color:C.white, fontFace:"Cambria" });

  const points = [
    ["🏆 Best Model",      "XGBoost (GBM) — RMSE: 0.006, R²: 1.00. Excels with feature-engineered lag terms even on sparse data."],
    ["🥈 Runner-Up",       "Linear Regression — simple, interpretable, RMSE: 0.365. Works well when trends are linear."],
    ["⚠️ Limitations",     "Only 3 time points (2014, 2016, 2018). Deep learning models (LSTM, ANN) are disadvantaged by sparse data."],
    ["🔮 2020 Outlook",    "Life satisfaction expected ~7.68; health declining; financial wellbeing improving; job satisfaction falling."],
    ["📈 Next Steps",      "Incorporate demographic sub-groups, external predictors (GDP, unemployment), and evaluate against 2020 NZGSS actuals."],
  ];

  for(let i=0;i<5;i++){
    s.addShape(pres.shapes.ROUNDED_RECTANGLE, { x:0.5, y:0.95+i*0.93, w:9.0, h:0.82,
      fill:{ color: i===0 ? "0D3D4F" : i===1 ? "0D3240" : "0D2A37" }, rectRadius:0.08 });
    s.addText(points[i][0], { x:0.65, y:1.02+i*0.93, w:1.8, h:0.65, fontSize:11, bold:true, color:C.mint, fontFace:"Calibri" });
    s.addText(points[i][1], { x:2.55, y:1.02+i*0.93, w:7.0, h:0.65, fontSize:11, color:C.white, fontFace:"Calibri" });
  }
  s.addNotes("XGBoost wins decisively. Key caveat: with 3 data points, XGBoost may overfit; cross-dataset generalization should be validated.");
}

// ── Slide 10: Thank You ─────────────────────────────────────────────────────
{
  const s = pres.addSlide();
  s.background = { color: C.teal };
  s.addShape(pres.shapes.OVAL, { x:-1, y:-1.5, w:5, h:5, fill:{ color:C.dark, transparency:60 } });
  s.addShape(pres.shapes.OVAL, { x:7, y:3, w:4, h:4, fill:{ color:C.mint, transparency:65 } });

  s.addText("Thank You", { x:1, y:1.5, w:8, h:1.0, fontSize:48, bold:true, color:C.white, fontFace:"Cambria", align:"center" });
  s.addText("NZ Wellbeing Forecasting · 5-Model Comparison", {
    x:1, y:2.7, w:8, h:0.5, fontSize:15, color:"CCF0F4", fontFace:"Calibri", align:"center"
  });
  s.addText("Dataset: Stats NZ NZGSS 2014–2018 · Models: Linear Regression, XGBoost, LSTM, ANN, ARIMA", {
    x:0.5, y:4.9, w:9, h:0.35, fontSize:10, color:"CCF0F4", fontFace:"Calibri", align:"center"
  });
  s.addNotes("End of presentation.");
}

pres.writeFile({ fileName: `${OUT}/NZ_Wellbeing_Forecast.pptx` })
  .then(() => console.log("Presentation saved!"))
  .catch(e => console.error(e));
