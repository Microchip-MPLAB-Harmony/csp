import React, { useState } from 'react';
import { ListBox } from 'primereact/listbox';
import { component_id } from './MainBlock';
import { AddBoldLabel, AddDivioType, CheckSelectedSymbolValue } from './CustomLabels';
import DropDown from '@mplab_harmony/harmony-plugin-ui/build/components/DropDown';
import CheckBox from '@mplab_harmony/harmony-plugin-ui/build/components/CheckBox';
import InputNumber from '@mplab_harmony/harmony-plugin-ui/build/components/InputNumber';
import {
  GetSymbolArray,
  GetSymbolMaxValue,
  GetSymbolMinValue,
  GetSymbolReadOnlyStatus,
  GetSymbolValue,
  GetSymbolVisibleStatus
} from '@mplab_harmony/harmony-plugin-core-service/build/database-access/SymbolAccess';
import { GetLabelWithCustomDisplay } from '@mplab_harmony/harmony-plugin-ui/build/components/Label';
import {
  GetMinFractionValueBasedSymbolType,
  GetStyle
} from '@mplab_harmony/harmony-plugin-ui/build/components/Components';
import { useBetween } from 'use-between';
import useInitService from '../../../InitService';

const ProgrammableClockController = (props: { parentUpdate: () => void }) => {
  const [value, setValue] = useState('PCK 0');
  const tabs = ['PCK 0', 'PCK 1'];

  function AddPCK(index: number) {
    return (
      <div className='p-fluid'>
        {AddCombobox('CLK_PCK' + index + '_CSS', 'CLK_PCK0_CSS')}
        {AddInputNumber('CLK_PCK' + index + '_PRES', 'CLK_PCK0_PRES')}
        {AddCheckBox('CLK_PCK' + index + '_EN', 'CLK_PCK0_EN')}
        {AddFrequencyLabel('CLK_PCK' + index + '_FREQUENCY', 'CLK_PCK0_FREQUENCY')}

        {AddDivioType(
          'label_pclkPresVal',
          GetSymbolValue(component_id, 'CLK_PCK' + index + '_PRES')
        )}

        {AddBoldLabel(
          'label_pclk_MD_SLCK',
          'MD_CLK',
          CheckSelectedSymbolValue('CLK_PCK' + index + '_CSS', 'MD_SLOW_CLK')
        )}
        {AddBoldLabel(
          'label_pclk_TD_SLCK',
          'TD_SLCK',
          CheckSelectedSymbolValue('CLK_PCK' + index + '_CSS', 'TD_SLOW_CLOCK')
        )}
        {AddBoldLabel(
          'label_pclk_MAINCK',
          'MAINCK',
          CheckSelectedSymbolValue('CLK_PCK' + index + '_CSS', 'MAINCK')
        )}
        {AddBoldLabel(
          'label_pclk_MANCK',
          'MCK',
          CheckSelectedSymbolValue('CLK_PCK' + index + '_CSS', 'MCK')
        )}
        {AddBoldLabel(
          'label_pclk_PLLACK',
          'PLLACK',
          CheckSelectedSymbolValue('CLK_PCK' + index + '_CSS', 'PLLA')
        )}
        {AddBoldLabel(
          'label_pclk_UPLLCK',
          'UPLLCK',
          CheckSelectedSymbolValue('CLK_PCK' + index + '_CSS', 'UPLL')
        )}
        {AddBoldLabel(
          'label_pclk_AUDIOPLLCK',
          'AUDIOPLLCK',
          CheckSelectedSymbolValue('CLK_PCK' + index + '_CSS', 'AUDIOPLL')
        )}
      </div>
    );
  }

  function AddFrequencyLabel(symbolId: string, styleId: string) {
    return (
      <div>
        <GetLabelWithCustomDisplay
          labelId={symbolId}
          labelDisplayText={GetSymbolValue(component_id, symbolId) + ' Hz'}
          labelStyle={GetStyle(styleId)}
        />
      </div>
    );
  }

  function AddCombobox(symbolId: string, styleId: string) {
    const { refreshScreen } = useBetween(useInitService);
    return (
      <div>
        <DropDown
          componentId={component_id}
          symbolId={symbolId}
          onChange={(e) => {
            refreshScreen();
            props.parentUpdate();
          }}
          symbolValue={GetSymbolValue(component_id, symbolId)}
          symbolArray={GetSymbolArray(component_id, symbolId)}
          styleObject={GetStyle(styleId)}
          symbolListeners={[symbolId]}
          readOnly={GetSymbolReadOnlyStatus(component_id, symbolId)}
          visible={GetSymbolVisibleStatus(component_id, symbolId)}
        />
      </div>
    );
  }

  function AddCheckBox(symbolId: string, styleId: string) {
    const { refreshScreen } = useBetween(useInitService);
    return (
      <div>
        <CheckBox
          componentId={component_id}
          symbolId={symbolId}
          onChange={(e) => {
            refreshScreen();
            props.parentUpdate();
          }}
          symbolValue={GetSymbolValue(component_id, symbolId)}
          styleObject={GetStyle(styleId)}
          symbolListeners={[symbolId]}
          readOnly={GetSymbolReadOnlyStatus(component_id, symbolId)}
          visible={GetSymbolVisibleStatus(component_id, symbolId)}
        />
      </div>
    );
  }

  function AddInputNumber(symbolId: string, styleId: string) {
    const { refreshScreen } = useBetween(useInitService);
    return (
      <div>
        <InputNumber
          componentId={component_id}
          symbolId={symbolId}
          onChange={(e) => {
            refreshScreen();
            props.parentUpdate();
          }}
          symbolValue={GetSymbolValue(component_id, symbolId)}
          minFractionValue={GetMinFractionValueBasedSymbolType(component_id, symbolId)}
          minValue={GetSymbolMinValue(component_id, symbolId)}
          maxValue={GetSymbolMaxValue(component_id, symbolId)}
          styleObject={GetStyle(styleId)}
          symbolListeners={[symbolId]}
          readOnly={GetSymbolReadOnlyStatus(component_id, symbolId)}
          visible={GetSymbolVisibleStatus(component_id, symbolId)}
        />
      </div>
    );
  }

  function NullSelected() {
    setValue('PCK 0');
    return <div>{AddPCK(0)}</div>;
  }

  return (
    <div className='card'>
      <ListBox
        value={value}
        options={tabs}
        style={GetStyle('button_pclkTab0')}
        onChange={(e) => setValue(e.value)}
      />
      {!value && NullSelected()}
      {value === 'PCK 0' && AddPCK(0)}
      {value === 'PCK 1' && AddPCK(1)}
    </div>
  );
};

export default ProgrammableClockController;
