/*******************************************************************************
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
 *******************************************************************************/
import { convertToBoolean } from '@mplab_harmony/harmony-plugin-ui/build/utils/CommonUtil';
import {
  ChangeValueState,
  SymbolChanged,
  ConfigSymbolEvent,
} from '@mplab_harmony/harmony-plugin-ui/build/utils/ComponentStateChangeUtils';
import ChannelTableView from './active-channel-table/ChannelTableView';
import ChannelSetting from './channel-setting/ChannelSetting';
import './main-view.css';

(window as any).SymbolValueChanged = (value: any) => {
  if (value == null) return;

  const symbolData = value.split('M*C');

  const symbol: ConfigSymbolEvent = {
    symbolID: symbolData[0],
    value: symbolData[1],
    readOnly: convertToBoolean(symbolData[2]),
    visible: convertToBoolean(symbolData[3]),
  };

  SymbolChanged(symbol);

  ChangeValueState(symbol.symbolID, symbol.value);
};

export default function MainView() {
  return (
    <div className="dma-main-view">
      <ChannelTableView />
      <ChannelSetting />
    </div>
  );
}
