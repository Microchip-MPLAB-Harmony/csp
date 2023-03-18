import { useEffect } from 'react';
import ClockSVG from '../../../Resources/Svgs/SAM9X7_clock.svg';
import symbolJSON from '../../../Resources/Json/symbol.json';
import { AddCustomLabels } from './CustomLabels';
import { AddCustomButtons, SummaryPageHeading, callPopUp } from './CustomButtons';
import TabbedButton from './PCKController/ProgrammableClockController';
import SummaryPage from './Summary';
import {
  ChangeValueState,
  SymbolChanged,
  ConfigSymbolEvent,
  CheckForSymbolLinkedLabel
} from '@mplab_harmony/harmony-plugin-ui/build/utils/ComponentStateChangeUtils';
import { convertToBoolean } from '@mplab_harmony/harmony-plugin-ui/build/utils/CommonUtil';
import { error } from '@mplab_harmony/harmony-plugin-core-service/build/log/CustomConsole';
import { SetComponentId } from '@mplab_harmony/harmony-plugin-core-service/build/database-access/SymbolAccess';
import {
  globalSymbolStyleData,
  StoreSymbolStyle
} from '@mplab_harmony/harmony-plugin-ui/build/components/Components';
import { GetUIComponentWithOutLabel } from '@mplab_harmony/harmony-plugin-ui/build/components/Components';
import FrequencyLabels from './FrequencyLabels';
import { Toolbar } from 'clock-common';
import GenericPopUp from './CustomPopUp';

export const component_id = 'core';
export const toolBarHeight = '60px';
const symbolsArray: string[] = [];
export const frequencyLabelsArray: string[] = [];
let symbolsStyle = new Map<any, any>();

let portNumber = (window as any).javaConnector.getPortNumber();

const dynamicSymbolsIgnoreList = [
  'CLK_PCK0_CSS',
  'CLK_PCK0_PRES',
  'CLK_PCK0_EN',
  'CLK_PCK0_FREQUENCY'
];

(window as any).SymbolValueChanged = (value: any) => {
  if (value == null) return;

  const symbolData = value.split('M*C');

  const symbol: ConfigSymbolEvent = {
    symbolID: symbolData[0],
    value: symbolData[1],
    readOnly: convertToBoolean(symbolData[2]),
    visible: convertToBoolean(symbolData[3])
  };

  SymbolChanged(symbol);

  ChangeValueState(symbol.symbolID, symbol.value);
  CheckForSymbolLinkedLabel(symbol.symbolID, symbol.value);
};

const MainBlock = () => {
  ReadJSONData(symbolJSON);
  SetComponentId('core');

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

  function AddSymbolLinkedUIComponents() {
    try {
      return <div className='p-fluid'>{symbolsArray.map((id: string) => AddComponent(id))}</div>;
    } catch (err) {
      error('Unable to create SymbolLinkedUIComponents: ' + err);
    }
  }

  return (
    <div>
      <div>{/* <Headder /> */}</div>
      <Toolbar
        title={'Clock Configuration'}
        helpUrl={'http://localhost:' + portNumber + '/csp/docs/index.html'}
        onClickSummary={function (): void {
          callPopUp(GenericPopUp, SummaryPageHeading, '95vw', '95vh');
        }}
      />
      <div
        className='card'
        id='home'>
        <img
          src={ClockSVG}
          alt='icon'
          style={{ width: '1300px', height: '1740px', top: '0px', left: '0px' }}
        />
        {AddSymbolLinkedUIComponents()}
        {AddCustomLabels()}
        {AddCustomButtons()}
        <FrequencyLabels />
        <TabbedButton />
      </div>
    </div>
  );
};

export default MainBlock;

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
