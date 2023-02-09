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
import InterruptTable from './InterruptTable';
import { Button } from 'primereact/button';
import { Toolbar } from 'primereact/toolbar';

import '../Styles/Header.css';
import React from 'react';
import { SetComponentId } from '@mplab_harmony/harmony-plugin-core-service/build/database-access/SymbolAccess';
import {
  ZoomInReact,
  ZoomOutReact,
} from '@mplab_harmony/harmony-plugin-core-service/build/project-service/ProjectService';
import { globalSymbolSStateData } from '@mplab_harmony/harmony-plugin-ui/build/components/Components';
import { convertToBoolean } from '@mplab_harmony/harmony-plugin-core-service/build/database-access/SymbolUtils';
import {
  ChangeReadOnlyState,
  ChangeValueState,
} from '@mplab_harmony/harmony-plugin-ui/build/utils/ComponentStateChangeUtils';

export let progressStatus = true;

export let component_id = 'core';
export let toolBarHeight = '60px';

let portNumber = (window as any).javaConnector.getPortNumber();

const MainBlock = () => {
  SetComponentId(component_id);

  const leftContents = (
    <React.Fragment>
      <label style={{ fontSize: '18px', fontWeight: 'bolder' }}>
        {' '}
        INTERRUPT CONFIGURATION{' '}
      </label>
    </React.Fragment>
  );

  const rightContents = (
    <React.Fragment>
      {/* <Button
        label="HOME"
        tooltip="View Interrupt Manager Home Screen"
        tooltipOptions={{ position: "bottom" }}
        icon="pi pi-home"
        iconPos="left"
        className="p-button p-button-text p-mr-2"
        style={{ fontWeight: "bold", color: "black" }}
        onClick={() => LoadHome()}
      /> */}
      <Button
        label="HELP"
        tooltip="View Interrupt Manager help"
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

  return (
    <div>
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
      <div className="card">
        <div id="nvic_main">
          <InterruptTable />
        </div>
      </div>
    </div>
  );
};

export default MainBlock;

(window as any).SymbolValueChanged = (value: any) => {
  if (value !== null && value !== undefined) {
    let symbolData = value.split('M*C');
    let symbolId = symbolData[0];
    let symbolValue = symbolData[1];
    // let editable = convertToBoolean(symbolData[2]);
    // let visible = convertToBoolean(symbolData[3]);

    if (symbolId.endsWith('_LOCK')) {
      if (globalSymbolSStateData.get(symbolId) != null) {
        symbolValue = convertToBoolean(symbolValue);
        ChangeReadOnlyState(symbolId, symbolValue);
      }
      return;
    }

    if (globalSymbolSStateData.get(symbolId) != null) {
      ChangeValueState(symbolId, symbolValue);
    }
  }
};
