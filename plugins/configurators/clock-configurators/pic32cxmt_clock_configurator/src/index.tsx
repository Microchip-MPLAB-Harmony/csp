import MainBlock from './ClockManager/UI/MainView/MainBlock';
import reportWebVitals from './ProjectConfig/reportWebVitals';

import 'primeicons/primeicons.css';
import 'primereact/resources/themes/nova/theme.css';
import 'primereact/resources/primereact.css';
import 'primeflex/primeflex.css';

import './Styles/index.css';

import ReactDOM from 'react-dom/client';

const root = ReactDOM.createRoot(
  document.getElementById('root') as HTMLElement
);

root.render(<MainBlock />);
reportWebVitals();
