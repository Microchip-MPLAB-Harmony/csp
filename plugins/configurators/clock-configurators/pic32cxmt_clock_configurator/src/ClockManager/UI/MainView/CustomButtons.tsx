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
import ReactDOM from 'react-dom';
import Button from '@mplab_harmony/harmony-plugin-ui/build/components/Button';
import { GetStyle } from '@mplab_harmony/harmony-plugin-ui/build/components/Components';
import GenericPopUp, { PopupLoaderId } from './CustomPopUp';

export let peripheralClockConfig_PopupHeadding = 'Peripheral Configuration';
export let GenerickClock_PopupHeadding = 'Generic Clock Configuration';
export let SummaryPageHeading = 'Clock Summary';

let styleMap = new Map<String, any>();
styleMap.set('width', '80%');
styleMap.set('height', '80%');

export function AddCustomButtons() {
  try {
    return (
      <div className="p-fluid">
        {AddButton(
          'button_PeripheralClock',
          'Peripherals',
          PeripheralButtonClicked
        )}

        {AddButton('button_GenericClock', 'Generic Clock', GenericClockClicked)}
      </div>
    );
  } catch (err) {}
}

function AddButton(
  id: string,
  buttonDisplayText: string,
  buttonClick: (arg0: any) => void
) {
  try {
    return (
      <Button
        buttonId={id}
        onChange={buttonClick}
        buttonDisplayText={buttonDisplayText}
        styleObject={GetStyle(id)}
      />
    );
  } catch (err) {}
}

function PeripheralButtonClicked() {
  callPopUp(GenericPopUp, peripheralClockConfig_PopupHeadding, '40vw', '95vh');
}

function GenericClockClicked() {
  callPopUp(GenericPopUp, GenerickClock_PopupHeadding, '50vw', '95vh');
}

export function callPopUp(
  Component: any,
  action_id: any,
  width: any,
  height: any
) {
  const createPopup = React.createElement(Component);
  PopupLoaderId(action_id, width, height);
  ReactDOM.render(createPopup, document.querySelector('#popup'));
}
