import React from 'react';
import { Button } from 'primereact/button';
import { Toolbar as PrimeToolbar } from 'primereact/toolbar';

import { HideDiv, ShowDiv } from '@mplab_harmony/harmony-plugin-ui/build/utils/NodeUtils';
import {
  ZoomInReact,
  ZoomOutReact
} from '@mplab_harmony/harmony-plugin-core-service/build/project-service/ProjectService';
import { pluginService } from './PluginService';

interface IProps {
  title: string;
  helpUrl: string;
  onClickSummary: () => void;
}

const Toolbar = (props: IProps) => {
  const leftContents = (
    <React.Fragment>
      <label style={{ fontSize: '18px', fontWeight: 'bolder' }}> {props.title} </label>
    </React.Fragment>
  );

  const rightContents = (
    <React.Fragment>
      {/* <Button
        label='HOME'
        tooltip={`View ${props.title} Home Screen`}
        tooltipOptions={{ position: 'bottom' }}
        icon='pi pi-home'
        iconPos='left'
        className='p-button p-button-text mr-2'
        style={{ fontWeight: 'bold', color: 'black' }}
        onClick={() => LoadHome()}
      /> */}
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
        onClick={() => pluginService.openURL(props.helpUrl)}
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
  };

  const LoadHome = () => {
    ShowDiv(document.getElementById('home'), null);
  };

  const LoadSummary = () => {
    props.onClickSummary();
  };

  function ZoomIn() {
    ZoomInReact();
  }

  function ZoomOut() {
    ZoomOutReact();
  }

  return (
    <div className='Headder'>
      <div>
        <PrimeToolbar
          left={leftContents}
          right={rightContents}
          style={{ background: 'white', height: 60, border: 'white' }}
        />
      </div>
    </div>
  );
};

export default Toolbar;
