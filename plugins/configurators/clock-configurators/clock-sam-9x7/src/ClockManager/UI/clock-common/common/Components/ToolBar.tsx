import React, { useState } from 'react';
import { Button } from 'primereact/button';
import { Toolbar } from 'primereact/toolbar';

import { Dialog } from 'primereact/dialog';

let portNumber = (window as any).javaConnector.getPortNumber();

const ToolBar = (props: {
  toolBarHeading: string;
  dialogHeading: string;
  widthValue: string;
  heightValue: string;
  childComponent: React.ReactNode;
  zoom: any;
}) => {
  const leftContents = (
    <React.Fragment>
      <label style={{ fontSize: '14px', fontWeight: 'bolder' }}> {props.toolBarHeading} </label>
    </React.Fragment>
  );

  const [dialogVisible, SetDialogVisible] = useState(false);

  const rightContents = (
    <React.Fragment>
      <Button
        label='SUMMARY'
        tooltip='View Summary'
        tooltipOptions={{ position: 'bottom' }}
        className='p-button p-button-text  p-mr-2'
        style={{ fontSize: '14px', fontWeight: 'bolder', color: 'black' }}
        onClick={() => LoadSummary()}
      />
      <Button
        label='HELP'
        tooltip='View help'
        tooltipOptions={{ position: 'bottom' }}
        // icon="pi pi-search"
        className='p-button p-button-text  p-mr-2'
        iconPos='right'
        style={{ fontSize: '14px', fontWeight: 'bolder', color: 'black' }}
        onClick={() => LoadHelp()}
      />
      <Button
        tooltip='Ctrl + Mouse Scroll Up'
        tooltipOptions={{ position: 'left' }}
        icon='pi pi-search-plus'
        style={{ color: 'black' }}
        className='p-button-rounded p-button-text p-button-plain p-button-lg p-mr-1'
        onClick={() => ZoomIn()}
      />
      <Button
        tooltip='Ctrl + Mouse Scroll Down'
        tooltipOptions={{ position: 'left' }}
        icon='pi pi-search-minus'
        style={{ color: 'black' }}
        className='p-button-rounded p-button-text p-button-lg p-button-plain'
        onClick={() => ZoomOut()}
      />
      {/* <Button
        tooltip='click here to reset zoom'
        tooltipOptions={{ position: 'left' }}
        icon='pi pi-fw pi-refresh'
        className='p-button-rounded p-button-text p-button-lg p-button-plain'
        onClick={() => ResetZoom()}
      /> */}
    </React.Fragment>
  );

  const LoadSummary = () => {
    SetDialogVisible(true);
  };

  const onDialogHide = () => {
    SetDialogVisible(false);
  };

  const LoadHelp = () => {
    window.open(
      'http://localhost:' + portNumber + '/motor_control/docs/index.html',
      '_blank',
      'toolbar=0,location=0,menubar=0'
    );
  };

  function ZoomIn() {
    props.zoom.zoomIn();
  }

  function ZoomOut() {
    props.zoom.zoomOut();
  }

  function ResetZoom() {
    props.zoom.resetZoom();
  }

  return (
    <div className='Headder'>
      <div>
        <Toolbar
          left={leftContents}
          right={rightContents}
          style={{
            background: 'white',
            height: '60px',
            maxHeight: '60px',
            border: 'white',
            top: '0',
            overflow: 'hidden'
          }}
        />
      </div>
      <div className='card p-mx-auto'>
        <Dialog
          visible={dialogVisible}
          maximizable={true}
          closeOnEscape
          closable
          focusOnShow
          modal
          header={props.dialogHeading}
          style={{ width: props.widthValue, height: props.heightValue, fontSize: '14px' }}
          onHide={() => onDialogHide()}>
          <div>{props.childComponent}</div>
        </Dialog>
      </div>
    </div>
  );
};

export default ToolBar;
