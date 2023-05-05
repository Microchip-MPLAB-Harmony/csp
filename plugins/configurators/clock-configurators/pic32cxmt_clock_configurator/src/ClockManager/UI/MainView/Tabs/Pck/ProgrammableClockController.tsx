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
import { GetStyle } from '@mplab_harmony/harmony-plugin-ui/build/components/Components';

import PCKFixedBoldLabelStatusUpdate from './PCKFixedBoldLabelStatusUpdate';
import {
  AddCheckBox,
  AddCombobox,
  AddInputNumber,
} from 'clock-common/lib/ClockUtils/ClockCommonUtils';
import { component_id } from '../../MainBlock';
import { AddPrefixDivSymbolLabel } from 'clock-common/lib/ClockUtils/ClockLabelUtils';
import { AddDivioType } from '../PLLController';

const ProgrammableClockController = () => {
  const [value, setValue] = useState('PCK 0');
  const tabs = ['PCK 0', 'PCK 1', 'PCK 2'];

  function AddPCK(index: number) {
    return (
      <div className="p-fluid">
        {AddCombobox(
          component_id,
          'CLK_PCK' + index + '_CSS',
          'tab_PCKx_combo_css'
        )}
        {AddInputNumber(
          component_id,
          'CLK_PCK' + index + '_PRES',
          'tab_PCKx_spinner_pres'
        )}
        {AddCheckBox(
          component_id,
          'CLK_SCER_PCK' + index,
          'tab_PCKx_checkBox_en'
        )}

        {AddPrefixDivSymbolLabel(
          'tab_label_pckxPresValue',
          component_id,
          'CLK_PCK' + index + '_PRES',
          AddDivioType
        )}

        <PCKFixedBoldLabelStatusUpdate
          symboListenerValue={'CLK_PCK' + index + '_CSS'}
        />
      </div>
    );
  }

  function NullSelected() {
    setValue('PCK 0');
    return <div>{AddPCK(0)}</div>;
  }

  return (
    <div className="card">
      <ListBox
        value={value}
        options={tabs}
        style={GetStyle('button_pckxClockTab')}
        onChange={(e) => setValue(e.value)}
      />
      {!value && NullSelected()}
      {value === 'PCK 0' && AddPCK(0)}
      {value === 'PCK 1' && AddPCK(1)}
      {value === 'PCK 2' && AddPCK(2)}
    </div>
  );
};

export default ProgrammableClockController;
