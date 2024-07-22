import 'primeicons/primeicons.css';
import 'primereact/resources/themes/nova/theme.css';
import 'primereact/resources/primereact.css';
import 'primeflex/primeflex.css';

import './Styles/index.css';
import ReactDOM from 'react-dom/client';
import TrustZoneMainView from './Main/MainView/TrustZoneMainView';
import React from 'react';
import { HarmonyContextProvider } from '@mplab_harmony/harmony-plugin-client-lib';

const root = ReactDOM.createRoot(document.getElementById('root') as HTMLElement);
root.render(
  <React.StrictMode>
    <HarmonyContextProvider>
      <TrustZoneMainView />
    </HarmonyContextProvider>
  </React.StrictMode>
);
