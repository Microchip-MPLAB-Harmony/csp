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
import { useState } from 'react';
import { ListBox } from 'primereact/listbox';
import { component_id, redColor } from '../MainBlock';
import { GetSymbolValue } from '@mplab_harmony/harmony-plugin-core-service/build/database-access/SymbolAccess';
import {
  AddCheckBox,
  AddCombobox,
  AddDummyCheckBox,
  AddDummyInputNumber,
  AddInputNumber,
} from 'clock-common/lib/ClockUtils/ClockCommonUtils';
import { GetStyle } from '@mplab_harmony/harmony-plugin-ui/build/components/Components';
import { error } from '@mplab_harmony/harmony-plugin-core-service/build/log/CustomConsole';
import {
  AddMinMaxSymboLabelWithSuffix,
  AddPlainLabel,
  AddPrefixDivSymbolLabel,
  AddSymboLabelWithSuffix,
} from 'clock-common/lib/ClockUtils/ClockLabelUtils';

const PLLController = () => {
  const [value, setValue] = useState('PLL A');
  const tabs = ['PLL A', 'PLL B', 'PLL C'];

  function AddPLL(letter: string) {
    try {
      const minCoreClockValue = GetSymbolValue(
        component_id,
        'PLL' + letter + '_MINCORECLK_FREQUENCY'
      );
      const maxCoreClockValue = GetSymbolValue(
        component_id,
        'PLL' + letter + '_MAXCORECLK_FREQUENCY'
      );

      return (
        <div className="p-fluid">
          {AddCombobox(
            component_id,
            'CLK_PLL' + letter + '_PLLMS',
            'tab_PLLA_combo_source'
          )}
          {AddInputNumber(
            component_id,
            'CLK_PLL' + letter + '_MUL',
            'tab_PLLA_spinner_mul'
          )}
          {AddSymboLabelWithSuffix(
            'tab_label_mulValue',
            component_id,
            'CLK_PLL' + letter + '_MUL',
            ''
          )}
          {AddInputNumber(
            component_id,
            'CLK_PLL' + letter + '_FRACR',
            'tab_PLLA_spinner_fracr'
          )}
          {AddSymboLabelWithSuffix(
            'tab_label_fracrValue',
            component_id,
            'CLK_PLL' + letter + '_FRACR',
            ''
          )}
          {AddInputNumber(
            component_id,
            'CLK_PLL' + letter + '_STEP',
            'tab_PLLA_spinner_step'
          )}
          {AddInputNumber(
            component_id,
            'CLK_PLL' + letter + '_NSTEP',
            'tab_PLLA_spinner_nstep'
          )}
          {AddInputNumber(
            component_id,
            'CLK_PLL' + letter + '_DIVPMC0',
            'tab_PLLA_spinner_divpmc0'
          )}

          {AddCheckBox(
            component_id,
            'CLK_PLL' + letter + '_ENPLL',
            'tab_PLLA_checkBox_enable'
          )}
          {AddCheckBox(
            component_id,
            'CLK_PLL' + letter + '_ENSPREAD',
            'tab_PLLA_checkBox_enspread'
          )}
          {AddCheckBox(
            component_id,
            'CLK_PLL' + letter + '_ENPLLO0',
            'tab_PLLA_checkBox_enpllo0'
          )}

          {AddSymboLabelWithSuffix(
            'tab_label_PLLA_refclockFreq',
            component_id,
            'PLL' + letter + '_REFCLK_FREQUENCY',
            ' Hz'
          )}

          {AddMinMaxSymboLabelWithSuffix(
            'tab_label_PLLA_coRefFrequency',
            component_id,
            'PLL' + letter + '_CORECLK_FREQUENCY',
            ' Hz',
            minCoreClockValue,
            maxCoreClockValue,
            redColor,
            'The core PLL' +
              letter +
              ' clock frequency value should be between ' +
              minCoreClockValue +
              ' and ' +
              maxCoreClockValue +
              ' Hz.'
          )}

          {AddPrefixDivSymbolLabel(
            'tab_PLLA_label_PLLDivPmc0',
            component_id,
            'CLK_PLL' + letter + '_DIVPMC0',
            AddDivioType
          )}

          {letter === 'A' && PLLAUnique(letter)}
          {(letter === 'B' || letter === 'C') && CommonPLLBandPLLC(letter)}
        </div>
      );
    } catch (err) {
      error(err);
    }
  }

  function PLLAUnique(letter: string) {
    return (
      <div>
        {AddInputNumber(
          component_id,
          'CLK_PLL' + letter + '_DIVPMC1',
          'tab_PLLA_spinner_divpmc1'
        )}
        {AddCheckBox(
          component_id,
          'CLK_PLL' + letter + '_ENPLLO1',
          'tab_PLLA_checkBox_enpllo1'
        )}
        {AddPrefixDivSymbolLabel(
          'tab_label_PLLA_PLLDivpmc1',
          component_id,
          'CLK_PLL' + letter + '_DIVPMC1',
          AddDivioType
        )}
      </div>
    );
  }

  function CommonPLLBandPLLC(letter: string) {
    return (
      <div>
        {AddDummyInputNumber('tab_PLLA_spinner_divpmc1')}
        {AddDummyCheckBox('tab_PLLA_checkBox_enpllo1')}
        {AddPlainLabel('tab_label_PLLA_PLLDivpmc1', 'NA')}
      </div>
    );
  }

  function NullSelected() {
    setValue('PLL A');
    return <div>{AddPLL('A')}</div>;
  }

  return (
    <div className="card">
      <ListBox
        value={value}
        options={tabs}
        style={GetStyle('button_PLLx')}
        onChange={(e) => setValue(e.value)}
      />
      {!value && NullSelected()}
      {value === 'PLL A' && AddPLL('A')}
      {value === 'PLL B' && AddPLL('B')}
      {value === 'PLL C' && AddPLL('C')}
    </div>
  );
};

export default PLLController;

export function AddDivioType(text: any) {
  try {
    let newvalue = '(' + text + '+1)';
    return '/ ' + newvalue;
  } catch (err) {}
}

// function AddDivpmcType(id: string, text: string) {
//   try {
//     let newvalue = '(2*(' + text + '+1))';
//     return '/ ' + newvalue;
//   } catch (err) {}
// }
