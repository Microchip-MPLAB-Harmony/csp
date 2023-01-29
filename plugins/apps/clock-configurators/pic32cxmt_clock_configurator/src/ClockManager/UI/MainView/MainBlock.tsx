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
import DualCoreClockSVG from '../../../Resources/Svgs/cleaned_PIC32CXMT_clock_dual_core.svg';
import SingleCoreClockSVG from '../../../Resources/Svgs/cleaned_PIC32CXMT_clock_single_core_new.svg';
import DualCoreJsonData from '../../../Resources/Json/dualCore_symbol.json';
import SingleCoreJsonData from '../../../Resources/Json/singleCore_symbol.json';
import Headder from './ToolBar';
import PCKxController from './Tabs/Pck/ProgrammableClockController';
import PLLController from './Tabs/PLLController';
import { AddCustomButtons } from './CustomButtons';
import { AddCoreCustomLabels } from './CoreCustomComponentsAndLabels';
import SummaryPage from './Summary';
import {
  GetSymbolValue,
  SetComponentId,
} from '@mplab_harmony/harmony-plugin-core-service/build/database-access/SymbolAccess';
import {
  GetUIComponentWithOutLabel,
  StoreSymbolStyle,
  globalSymbolSStateData,
  globalSymbolStyleData,
} from '@mplab_harmony/harmony-plugin-ui/build/components/Components';
import {
  ChangeValueState,
  CheckForSymbolLinkedLabel,
} from '@mplab_harmony/harmony-plugin-ui/build/utils/ComponentStateChangeUtils';
import FrequencyLabels from './FrequencyLabels';

let symbolsStyle = new Map<any, any>();
export let component_id = 'core';
export let toolBarHeight = '60px';
export let redColor = 'red';
let symbolsArray: string[] = [];
export let frequencyLabelsArray: string[] = [];

let dynamicSymbolsIgnoreList: string | string[] = [
  'CLK_CPU_CKR_RATIO_MCK0DIV',
  'CLK_CPU_CKR_RATIO_MCK0DIV2',
  'CLK_CPU_CKR_RATIO_MCK1DIV',
];

let SelectedCore = GetSymbolValue(component_id, 'CoreSeries');
let DualCoreSeries = ['PIC32CXMTC', 'PIC32CXMTSH'];
let SingleCoreSeries = ['PIC32CXMTG'];
export let dualCoreString = 'DualCore';
export let singleCoreString = 'SingleCore';

export function GetCoreStatus() {
  if (DualCoreSeries.includes(SelectedCore)) {
    return dualCoreString;
  } else if (SingleCoreSeries.includes(SelectedCore)) {
    return singleCoreString;
  }
  return singleCoreString;
}

const MainBlock = () => {
  SetComponentId(component_id);
  ReadJSON();

  function AddComponent(id: string) {
    function ValueChange(onChangeData: Map<String, any>) {
      // do nothing
    }
    return (
      <div>
        <GetUIComponentWithOutLabel
          componentId={component_id}
          symbolId={id}
          onChange={ValueChange}
          symbolListeners={[id]}
        />
      </div>
    );
  }

  function AddDynamicSymbolLinkedUIComponents() {
    try {
      return (
        <div className="p-fluid">
          {symbolsArray.map((id: string) => AddComponent(id))}
        </div>
      );
    } catch (err) {}
  }

  function LoadCoreSVG(svg: any) {
    return (
      <div>
        <img
          src={svg}
          alt="icon"
          style={{ width: '1764px', height: '1548px', top: '0px', left: '0px' }}
        />
      </div>
    );
  }

  return (
    <div>
      <div>
        <Headder />
      </div>
      <div className="card">
        {GetCoreStatus() === dualCoreString && LoadCoreSVG(DualCoreClockSVG)}
        {GetCoreStatus() === singleCoreString &&
          LoadCoreSVG(SingleCoreClockSVG)}
        {AddCoreCustomLabels()}
        {AddDynamicSymbolLinkedUIComponents()}
        {AddCustomButtons()}

        <FrequencyLabels />
        <PCKxController />
        <PLLController />
      </div>
      <div id="summary" style={{ display: 'none' }}>
        {' '}
        <SummaryPage />{' '}
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
    if (globalSymbolSStateData.get(symbolId) != null) {
      ChangeValueState(symbolId, symbolValue);
    }
    CheckForSymbolLinkedLabel(symbolId, symbolValue);
  }
};

export function ReadJSON() {
  if (GetCoreStatus() === dualCoreString) {
    ReadJSONData(DualCoreJsonData);
  } else if (GetCoreStatus() === singleCoreString) {
    ReadJSONData(SingleCoreJsonData);
  }
}

function ReadJSONData(jsondata: any) {
  symbolsArray.length = 0;
  frequencyLabelsArray.length = 0;
  globalSymbolStyleData.clear();
  let symbolsData: any = jsondata;
  for (let prop in symbolsData) {
    let settings = symbolsData[prop];
    if (prop.startsWith('sym_')) {
      prop = prop.replace('sym_', '');
      if (!dynamicSymbolsIgnoreList.includes(prop)) {
        symbolsArray.push(prop);
      }
    } else if (prop.startsWith('label_sym_')) {
      prop = prop.replace('label_sym_', '');
      if (!dynamicSymbolsIgnoreList.includes(prop)) {
        frequencyLabelsArray.push(prop);
      }
    }
    for (let temp in settings) {
      symbolsStyle.set(prop, settings[temp]);
    }
    StoreSymbolStyle(toolBarHeight, prop, symbolsStyle);
  }
}
