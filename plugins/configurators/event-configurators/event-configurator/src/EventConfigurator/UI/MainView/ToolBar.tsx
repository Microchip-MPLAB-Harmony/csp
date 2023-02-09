import React from 'react';
import styles from './Toolbar.module.css';
import PrimeReact from 'primereact/api';

const Header = () => {
  PrimeReact.ripple = true;
  return <div className={styles.Header}>EVENT CONFIGURATOR</div>;
};

export default Header;
