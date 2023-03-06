import React from 'react';
import { Button } from 'primereact/button';
import { Toolbar } from 'primereact/toolbar';
import icon from '../../../Resources/Images/MICH4C.png';

import '../../../Styles/Headder.css';
import PrimeReact from 'primereact/api';
import { toolBarHeight } from './MainBlock';
import {
  HideDiv,
  LoadImage,
  ShowDiv
} from '@mplab_harmony/harmony-plugin-ui/build/utils/NodeUtils';
import {
  ZoomInReact,
  ZoomOutReact
} from '@mplab_harmony/harmony-plugin-core-service/build/project-service/ProjectService';
import { pluginService } from 'clock-common';

const portNumber = (window as any).javaConnector.getPortNumber();

const Headder = () => {
  PrimeReact.ripple = true;

  const leftContents = (
    <React.Fragment>
      {LoadImage(icon)}
      <label style={{ fontSize: '18px', fontWeight: 'bolder' }}> CLOCK CONFIGURATION </label>
    </React.Fragment>
  );

  const rightContents = (
    <React.Fragment>
      <Button
        label='HOME'
        tooltip='View Clock Configuration Home Screen'
        tooltipOptions={{ position: 'bottom' }}
        icon='pi pi-home'
        iconPos='left'
        className='p-button p-button-text mr-2'
        style={{ fontWeight: 'bold', color: 'black' }}
        onClick={() => LoadHome()}
      />
      <Button
        label='SUMMARY'
        tooltip='View Summary'
        tooltipOptions={{ position: 'bottom' }}
        className='p-button p-button-text  mr-2'
        style={{ fontWeight: 'bold', color: 'black' }}
        onClick={() => LoadSummary()}
      />
      <Button
        label='HELP'
        tooltip='View Clock Configuration help'
        tooltipOptions={{ position: 'bottom' }}
        // icon="pi pi-search"
        className='p-button p-button-text  mr-2'
        iconPos='right'
        style={{ fontWeight: 'bold', color: 'black' }}
        onClick={() => pluginService.openURL('csp/docs/index.html')}
      />
      <Button
        tooltip='Ctrl + Mouse Scroll Up'
        tooltipOptions={{ position: 'left' }}
        icon='pi pi-search-plus'
        className='p-button-rounded p-button-text p-button-plain p-button-lg mr-1'
        onClick={() => ZoomIn()}
      />
      <Button
        tooltip='Ctrl + Mouse Scroll Down'
        tooltipOptions={{ position: 'left' }}
        icon='pi pi-search-minus'
        className='p-button-rounded p-button-text p-button-lg p-button-plain'
        onClick={() => ZoomOut()}
      />
    </React.Fragment>
  );

  const HideAll = () => {
    HideDiv(document.getElementById('home'));
    HideDiv(document.getElementById('summary'));
  };

  const LoadHome = () => {
    HideAll();
    ShowDiv(document.getElementById('home'), null);
  };

  const LoadSummary = () => {
    HideAll();
    ShowDiv(document.getElementById('summary'), null);
  };

  const LoadHelp = () => {
    window.open(
      'http://localhost:' + portNumber + '/csp/docs/index.html',
      '_blank',
      'toolbar=0,location=0,menubar=0'
    );
  };

  function ZoomIn() {
    ZoomInReact();
  }

  function ZoomOut() {
    ZoomOutReact();
  }

  function openInNewTab(href: any) {
    Object.assign(document.createElement('a'), {
      target: '_blank',
      href: href
    }).click();
  }

  return (
    <div className='Headder'>
      <div>
        <Toolbar
          left={leftContents}
          right={rightContents}
          style={{ background: 'white', height: toolBarHeight, border: 'white' }}
        />
      </div>
    </div>
  );
};

export default Headder;
