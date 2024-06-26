import { useState } from 'react';
import { ListBox } from 'primereact/listbox';
import { component_id } from '../MainBlock';
import { GetStyle } from '@mplab_harmony/harmony-plugin-ui/build/components/Components';
import {
  AddCheckBox,
  AddCombobox,
  AddInputNumber
} from '../../clock-common/utils/ClockCommonUtils';
import { AddDivioType } from '../CustomLabels';
import PCKFixedBoldLabelStatusUpdate from './PCKFixedBoldLabelStatusUpdate';
import {
  AddInputFormatSymbolLabel,
  AddSymboLabelWithSuffix
} from '../../clock-common/utils/ClockLabelUtils';

const ProgrammableClockController = () => {
  const [value, setValue] = useState('PCK 0');
  const tabs = ['PCK 0', 'PCK 1'];
  alert(GetStyle('CLK_PCK0_CSS'));
  function AddPCK(index: number) {
    return (
      <div className='p-fluid'>
        {}
        <AddCombobox
          component_id={component_id}
          symbolId={'CLK_PCK' + index + '_CSS'}
          className={''}
          styleObj={GetStyle('CLK_PCK0_CSS')}
        />
        <AddInputNumber
          component_id={component_id}
          symbolId={'CLK_PCK' + index + '_PRES'}
          className={''}
          styleObj={GetStyle('CLK_PCK0_PRES')}
        />
        <AddCheckBox
          component_id={component_id}
          symbolId={'CLK_PCK' + index + '_EN'}
          className={''}
          styleObj={GetStyle('CLK_PCK0_EN')}
        />

        {AddSymboLabelWithSuffix(
          'CLK_PCK0_FREQUENCY',
          component_id,
          'CLK_PCK' + index + '_FREQUENCY',
          ' Hz'
        )}

        {AddInputFormatSymbolLabel(
          'label_pclkPresVal',
          component_id,
          'CLK_PCK' + index + '_PRES',
          AddDivioType
        )}

        <PCKFixedBoldLabelStatusUpdate symboListenerValue={'CLK_PCK' + index + '_CSS'} />
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
