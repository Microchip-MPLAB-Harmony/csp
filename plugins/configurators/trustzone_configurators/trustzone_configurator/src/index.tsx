import 'primeicons/primeicons.css';
import 'primereact/resources/themes/nova/theme.css';
import 'primereact/resources/primereact.css';
import 'primeflex/primeflex.css';

import './Styles/index.css';
import ReactDOM from 'react-dom/client';
import React from 'react';
import TrustZoneMainView from './Main/MainView/TrustZoneMainView';
import reportWebVitals from './ProjectConfig/reportWebVitals';

const root = ReactDOM.createRoot(
  document.getElementById('root') as HTMLElement
);

root.render(
  <React.StrictMode>
    <TrustZoneMainView />
  </React.StrictMode>
);
reportWebVitals();
