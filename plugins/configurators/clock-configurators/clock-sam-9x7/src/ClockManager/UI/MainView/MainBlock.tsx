import React, { useEffect } from 'react';
import ClockSVG from '../../../Resources/Svgs/SAM9X7_clock.svg';
import symbolJSON from '../../../Resources/Json/symbol.json';
import { AddCustomLabels } from './CustomLabels';
import { AddCustomButtons } from './CustomButtons';
import TabbedButton from './ProgrammableClockController';
import SummaryPage from './Summary';
import {
  ChangeValueState,
  SymbolChanged,
  ConfigSymbolEvent
} from '@mplab_harmony/harmony-plugin-ui/build/utils/ComponentStateChangeUtils';
import { convertToBoolean } from '@mplab_harmony/harmony-plugin-ui/build/utils/CommonUtil';
import useInitService, { refreshFullScreen } from '../../../InitService';
import { error, info } from '@mplab_harmony/harmony-plugin-core-service/build/log/CustomConsole';
import { GetLabelWithCustomDisplay } from '@mplab_harmony/harmony-plugin-ui/build/components/Label';
import {
  GetSymbolValue,
  SetComponentId
} from '@mplab_harmony/harmony-plugin-core-service/build/database-access/SymbolAccess';
import {
  GetStyle,
  globalSymbolStyleData,
  StoreSymbolStyle
} from '@mplab_harmony/harmony-plugin-ui/build/components/Components';
import { GetUIComponentWithOutLabel } from '@mplab_harmony/harmony-plugin-ui/build/components/Components';
import { greetIT } from 'clock-common/lib/Util';

export const component_id = 'core';
export const toolBarHeight = '60px';
const symbolsArray: string[] = [];
const labelsArray: string[] = [];

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

  refreshFullScreen();
};

const MainBlock = () => {
  const { refreshScreen } = useInitService();

  useEffect(() => {
    ReadJSONData();

    SetComponentId('core');

    greetIT('kathir');

    refreshScreen();
  }, []);

  function AddNonSymbolLinkedLabels() {
    try {
      return (
        <div className='p-fluid'>
          {labelsArray.map((id: string) => (
            <GetLabelWithCustomDisplay
              key={id}
              labelId={id}
              labelDisplayText={GetSymbolValue(component_id, id) + ' Hz'}
              labelStyle={GetStyle(id)}
            />
          ))}
        </div>
      );
    } catch (err) {
      error('Unable to create NonSymbolLinkedLabels: ' + err);
    }
  }

  function AddSymbolLinkedUIComponents() {
    try {
      return (
        <div className='p-fluid'>
          {symbolsArray.map((id: string) => (
            <GetUIComponentWithOutLabel
              key={id}
              componentId={component_id}
              symbolId={id}
              onChange={refreshScreen}
              symbolListeners={[id]}
            />
          ))}
        </div>
      );
    } catch (err) {
      error('Unable to create SymbolLinkedUIComponents: ' + err);
    }
  }

  return (
    <div>
      <div>
        <Toolbar />
      </div>
      <div
        className='card'
        id='home'>
        <img
          src={ClockSVG}
          alt='icon'
          style={{ width: '1300px', height: '1740px', top: '0px', left: '0px' }}
        />
        {AddSymbolLinkedUIComponents()}
        {AddNonSymbolLinkedLabels()}
        {AddCustomLabels()}
        {AddCustomButtons()}
        <TabbedButton parentUpdate={refreshScreen} />
      </div>
      <div
        id='summary'
        style={{ display: 'none' }}>
        <SummaryPage />{' '}
      </div>
    </div>
  );
};

export default MainBlock;

export function ReadJSONData() {
  const symbolsStyle = new Map<any, any>();
  symbolsArray.length = 0;
  labelsArray.length = 0;
  globalSymbolStyleData.clear();
  const symbolsData: any = symbolJSON;
  for (let prop in symbolsData) {
    const settings = symbolsData[prop];
    if (prop.startsWith('sym_')) {
      prop = prop.replace('sym_', '');
      if (!dynamicSymbolsIgnoreList.includes(prop)) {
        symbolsArray.push(prop);
      }
    } else if (prop.startsWith('label_sym_')) {
      prop = prop.replace('label_sym_', '');
      if (!dynamicSymbolsIgnoreList.includes(prop)) {
        labelsArray.push(prop);
      }
    }
    for (const temp in settings) {
      symbolsStyle.set(prop, settings[temp]);
    }
    StoreSymbolStyle(toolBarHeight, prop, symbolsStyle);
  }
}
