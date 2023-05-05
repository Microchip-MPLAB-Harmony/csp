/*
 * Copyright (C) 2022 Microchip Technology Inc. and its subsidiaries.
 *
 * Subject to your compliance with these terms, you may use Microchip software
 * and any derivatives exclusively with Microchip products. It is your
 * responsibility to comply with third party license terms applicable to your
 * use of third party software (including open source software) that may
 * accompany Microchip software.
 *
 * THIS SOFTWARE IS SUPPLIED BY MICROCHIP "AS IS". NO WARRANTIES, WHETHER
 * EXPRESS, IMPLIED OR STATUTORY, APPLY TO THIS SOFTWARE, INCLUDING ANY IMPLIED
 * WARRANTIES OF NON-INFRINGEMENT, MERCHANTABILITY, AND FITNESS FOR A
 * PARTICULAR PURPOSE.
 *
 * IN NO EVENT WILL MICROCHIP BE LIABLE FOR ANY INDIRECT, SPECIAL, PUNITIVE,
 * INCIDENTAL OR CONSEQUENTIAL LOSS, DAMAGE, COST OR EXPENSE OF ANY KIND
 * WHATSOEVER RELATED TO THE SOFTWARE, HOWEVER CAUSED, EVEN IF MICROCHIP HAS
 * BEEN ADVISED OF THE POSSIBILITY OR THE DAMAGES ARE FORESEEABLE. TO THE
 * FULLEST EXTENT ALLOWED BY LAW, MICROCHIP'S TOTAL LIABILITY ON ALL CLAIMS IN
 * ANY WAY RELATED TO THIS SOFTWARE WILL NOT EXCEED THE AMOUNT OF FEES, IF ANY,
 * THAT YOU HAVE PAID DIRECTLY TO MICROCHIP FOR THIS SOFTWARE.
 */
import React from 'react';
import { Button } from 'primereact/button';
import { Toolbar } from 'primereact/toolbar';

import '../../../Styles/Headder.css';
import PrimeReact from 'primereact/api';
import { toolBarHeight } from './MainBlock';
import {
  ZoomInReact,
  ZoomOutReact,
} from '@mplab_harmony/harmony-plugin-core-service/build/project-service/ProjectService';
import { SummaryPageHeading, callPopUp } from './CustomButtons';
import GenericPopUp from './CustomPopUp';

let portNumber = (window as any).javaConnector.getPortNumber();

const Headder = () => {
  PrimeReact.ripple = true;

  const leftContents = (
    <React.Fragment>
      {/* {LoadImage(icon)} */}
      <label style={{ fontSize: '18px', fontWeight: 'bolder' }}>
        {' '}
        CLOCK CONFIGURATION{' '}
      </label>
    </React.Fragment>
  );

  const rightContents = (
    <React.Fragment>
      {/* <Button
        label="HOME"
        tooltip="View Clock Home Screen"
        tooltipOptions={{ position: 'bottom' }}
        icon="pi pi-home"
        iconPos="left"
        className="p-button p-button-text p-mr-2"
        style={{ fontWeight: 'bold', color: 'black' }}
        onClick={() => LoadHome()}
      /> */}
      <Button
        label="SUMMARY"
        tooltip="View Summary"
        tooltipOptions={{ position: 'bottom' }}
        className="p-button p-button-text  p-mr-2"
        style={{ fontWeight: 'bold', color: 'black' }}
        onClick={() => LoadSummary()}
      />
      <Button
        label="HELP"
        tooltip="View Clock help"
        tooltipOptions={{ position: 'bottom' }}
        // icon="pi pi-search"
        className="p-button p-button-text  p-mr-2"
        iconPos="right"
        style={{ fontWeight: 'bold', color: 'black' }}
        onClick={() => LoadHelp()}
      />
      <Button
        tooltip="Ctrl + Mouse Scroll Up"
        tooltipOptions={{ position: 'left' }}
        icon="pi pi-search-plus"
        className="p-button-rounded p-button-text p-button-plain p-button-lg p-mr-1"
        onClick={() => ZoomIn()}
      />
      <Button
        tooltip="Ctrl + Mouse Scroll Down"
        tooltipOptions={{ position: 'left' }}
        icon="pi pi-search-minus"
        className="p-button-rounded p-button-text p-button-lg p-button-plain"
        onClick={() => ZoomOut()}
      />
    </React.Fragment>
  );

  const LoadSummary = () => {
    callPopUp(GenericPopUp, SummaryPageHeading, '95vw', '95vh');
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
      href: href,
    }).click();
  }

  return (
    <div className="Headder">
      <div>
        <Toolbar
          left={leftContents}
          right={rightContents}
          style={{
            background: 'white',
            height: toolBarHeight,
            border: 'white',
          }}
        />
      </div>
    </div>
  );
};

export default Headder;
