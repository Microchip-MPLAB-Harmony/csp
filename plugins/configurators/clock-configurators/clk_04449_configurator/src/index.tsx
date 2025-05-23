import React from 'react';
import ReactDOM from 'react-dom/client';

import 'primeicons/primeicons.css';
import 'primereact/resources/themes/nova/theme.css';
import 'primereact/resources/primereact.css';
import 'primeflex/primeflex.css';

import './index.css';
import { HarmonyContextProvider } from '@mplab_harmony/harmony-plugin-client-lib';
import MainBlock from './ClockManager/MainBlock';

const root = ReactDOM.createRoot(document.getElementById('root') as HTMLElement);
root.render(
  <React.StrictMode>
    <HarmonyContextProvider>
      <MainBlock />
    </HarmonyContextProvider>
  </React.StrictMode>
);
