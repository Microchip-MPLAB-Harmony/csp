import { log } from '@mplab_harmony/harmony-plugin-core-service/build/log/CustomConsole';
import Button from '@mplab_harmony/harmony-plugin-ui/build/components/Button';
import { GetStyle } from '@mplab_harmony/harmony-plugin-ui/build/components/Components';
import React from 'react';
import ReactDOM from 'react-dom';
import GenericPopUp, { PopupLoaderId } from '../CustomPopUp/CustomPopUp';

export const peripheralClockConfig_PopupHeadding = 'Peripheral Configuration';
export const GenerickClock_PopupHeadding = 'Generic Clock Configuration';

export function AddCustomButtons() {
  try {
    return (
      <div className='p-fluid'>
        {AddButton('button_peripheralClockConfig', 'Peripherals', PeripheralButtonClicked)}

        {AddButton('button_genericClockCtrl', 'Generic Clock', GenericClockClicked)}
      </div>
    );
  } catch (err) {
    /* empty */
  }
}

function AddButton(id: string, buttonDisplayText: string, buttonClick: (arg0: any) => void) {
  try {
    return (
      <Button
        buttonId={id}
        onChange={buttonClick}
        buttonDisplayText={buttonDisplayText}
        tooltip={'View Configurations'}
        tooltipPosition={'bottom'}
        readOnly={false}
        className='p-button-raised p-button-rounded'
        styleObject={GetStyle(id)}
        visible={true}
      />
    );
  } catch (err) {
    /* empty */
  }
}

function PeripheralButtonClicked() {
  callPopUp(GenericPopUp, peripheralClockConfig_PopupHeadding);
}

function GenericClockClicked() {
  callPopUp(GenericPopUp, GenerickClock_PopupHeadding);
}

function callPopUp(Component: any, action_id: any) {
  const createPopup = React.createElement(Component);
  PopupLoaderId(action_id);
  ReactDOM.render(createPopup, document.querySelector('#popup'));
}
