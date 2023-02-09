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
import Headder from './ToolBar';
import InterruptTable, { PriorityChanged } from './InterruptTable';
import { SetComponentId } from '@mplab_harmony/harmony-plugin-core-service/build/database-access/SymbolAccess';
import { UpdateRowAndVectorInterruptMap } from './Script';
import {
  ChangeReadOnlyState,
  ChangeValueState,
  globalSymbolSStateData,
} from '@mplab_harmony/harmony-plugin-ui';
import { info } from '@mplab_harmony/harmony-plugin-core-service/build/log/CustomConsole';

export let progressStatus = true;

export let component_id = 'core';
export let toolBarHeight = '60px';

const MainBlock = () => {
  SetComponentId(component_id);
  UpdateRowAndVectorInterruptMap();

  return (
    <div>
      <div>
        <Headder />
      </div>
      <div className="card">
        <div id="interrupt">
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
      ChangeReadOnlyState(symbolId, symbolValue);
      return;
    }

    ChangeValueState(symbolId, symbolValue);

    if (symbolId.endsWith('_PRIORITY')) {
      let nvicID = symbolId.split('_')[1] + '_';
      PriorityChanged(symbolValue, nvicID);
    }
  }
};
