import { Button } from 'primereact/button';
import React from 'react';
import { Toolbar } from 'primereact/toolbar';
import { SetComponentId } from '@mplab_harmony/harmony-plugin-core-service/build/database-access/SymbolAccess';
import {
  ZoomInReact,
  ZoomOutReact,
} from '@mplab_harmony/harmony-plugin-core-service/build/project-service/ProjectService';
import {
  ChangeValueState,
  ConfigSymbolEvent,
  SymbolChanged,
} from '@mplab_harmony/harmony-plugin-ui/build/utils/ComponentStateChangeUtils';
import '../../Styles/memory.css';
import { TabPanel, TabView } from 'primereact/tabview';
import Peripheral from '../Peripheral/Peripheral';
import Memory from '../Memory/Memory';
import { convertToBoolean } from '@mplab_harmony/harmony-plugin-core-service/build/database-access/SymbolUtils';

export let progressStatus = true;

export let component_id = 'core';
export let toolBarHeight = '60px';
export let secureColor = 'var(--green-500)';
export let nonSecureCallableColor = 'var(--green-300)';
export let nonSecureColor = 'var(--orange-500)';
export let fixedRegionColor = 'var(--gray-300)';
let portNumber = (window as any).javaConnector.getPortNumber();

let headingName = 'Arm\u00AE TrustZone\u00AE for Armv8-M';

const MainBlock = () => {
  SetComponentId(component_id);

  const leftContents = (
    <React.Fragment>
      {/* {LoadImage(icon)} */}
      <label style={{ fontSize: '18px', fontWeight: 'bolder' }}>
        {' '}
        {headingName}{' '}
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
        tooltip="View TrustZone Configurator help"
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
    <div className="card">
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
      <div>
        <TabView>
          <TabPanel header="Memory Configuration">
            <Memory />
          </TabPanel>
          <TabPanel header="Peripheral Configuration">
            <Peripheral />
          </TabPanel>
        </TabView>
      </div>
    </div>
  );
};

export default MainBlock;

(window as any).SymbolValueChanged = (value: any) => {
  if (value !== null && value !== undefined) {
    let symbolData = value.split('M*C');
    const symbol: ConfigSymbolEvent = {
      symbolID: symbolData[0],
      value: symbolData[1],
      readOnly: convertToBoolean(symbolData[2]),
      visible: convertToBoolean(symbolData[3]),
    };

    SymbolChanged(symbol);
  }
};
