import React from 'react';
import ReactDOM from 'react-dom';
import MainBlock from './ClockManager/UI/MainView/MainBlock';
import reportWebVitals from './ProjectConfig/reportWebVitals';

import "primeicons/primeicons.css";
import "primereact/resources/themes/saga-blue/theme.css";
import "primereact/resources/primereact.css";
import "primeflex/primeflex.css";

import "./Styles/index.css";
import { ReadJSONData } from './ClockManager/UI/MainView/MainBlock';


ReactDOM.render(
  <React.StrictMode>
    {ReadJSONData()}
    <MainBlock />
  </React.StrictMode>,
  document.getElementById('root')
);
reportWebVitals();
