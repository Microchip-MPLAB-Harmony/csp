import React from 'react';
import ReactDOM from 'react-dom';
import MainBlock from './ClockManager/UI/MainView/MainBlock';
import reportWebVitals from './ProjectConfig/reportWebVitals';

import 'primeicons/primeicons.css';
import 'primereact/resources/themes/saga-blue/theme.css';
import 'primereact/resources/primereact.css';
import 'primeflex/primeflex.css';

import './Styles/index.css';

ReactDOM.render(<MainBlock />, document.getElementById('root'));
reportWebVitals();
