import React from "react";
import ReactDOM from "react-dom";
import MainBlock from "./InterruptManager/UI/MainView/MainBlock";
import reportWebVitals from "./ProjectConfig/reportWebVitals";

import "primeicons/primeicons.css";
import "primereact/resources/themes/saga-blue/theme.css";
import "primereact/resources/primereact.css";
import "primeflex/primeflex.css";

import "./Styles/index.css";
import { UpdateRowAndVectorInterruptMap } from "./InterruptManager/UI/MainView/Script";
import ShowProgress from "./InterruptManager/UI/MainView/Progress";

ReactDOM.render(
  <React.StrictMode>
    {/* <ShowProgress /> */}
    {UpdateRowAndVectorInterruptMap()}
    <MainBlock />
  </React.StrictMode>,
  document.getElementById("root")
);
reportWebVitals();
