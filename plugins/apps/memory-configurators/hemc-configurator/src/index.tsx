import React from "react";
import ReactDOM from "react-dom/client";
import MainBlock from "./MemoryConfigurator/UI/MainView/MainBlock";

import "primeicons/primeicons.css";
import "primereact/resources/themes/nova/theme.css";
import "primereact/resources/primereact.css";
import "primeflex/primeflex.css";

import "./Styles/index.css";

const root = ReactDOM.createRoot(
  document.getElementById("root") as HTMLElement
);

root.render(
  <React.StrictMode>
    <MainBlock />
  </React.StrictMode>
);
