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

import { DataTable } from 'primereact/datatable';
import { Column } from 'primereact/column';
import { useContext } from 'react';
import {
  CheckBoxDefault,
  DropDownDefault,
  PluginConfigContext,
  useComboSymbol,
  useStringSymbol
} from '@mplab_harmony/harmony-plugin-client-lib';
import FrequencyLabelComponent from 'clock-common/lib/Components/LabelComponent/FrequencyLabelComponent';

const GenericClockConfiguration = () => {
  const { componentId = 'core' } = useContext(PluginConfigContext);

  const gclk_ids = useComboSymbol({
    componentId,
    symbolId: 'GCLK_IO_CLOCK_CONFIG_UI'
  });

  let channelPeripipheralMap = gclk_ids.options;
  let customLabelsArray = createCustomLengthArray();

  function createCustomLengthArray() {
    let dataArr = [];
    for (let i = 0; i < channelPeripipheralMap.length; i++) {
      dataArr.push({ id: i });
    }
    return dataArr;
  }

  const PeripheralBodyTemplate = (rowData: any) => {
    const stringSymbol = useStringSymbol({
      componentId: componentId,
      symbolId: channelPeripipheralMap[rowData.id] + '_NAME'
    });
    return <div>{stringSymbol.value}</div>;
  };

  const EnableBodyTemplate = (rowData: any) => {
    return (
      <div>
        <CheckBoxDefault
          componentId={componentId}
          symbolId={channelPeripipheralMap[rowData.id] + '_CHEN'}
        />
      </div>
    );
  };

  const SourceBodyTemplate = (rowData: any) => {
    return (
      <div>
        <DropDownDefault
          componentId={componentId}
          symbolId={channelPeripipheralMap[rowData.id] + '_GENSEL'}
        />
      </div>
    );
  };

  const FrequencyBodyTemplate = (rowData: any) => {
    return (
      <div>
        <FrequencyLabelComponent
          componentId={componentId}
          symbolId={channelPeripipheralMap[rowData.id] + '_FREQ'}
          className={''}
        />
      </div>
    );
  };

  return (
    <div>
      <DataTable
        value={customLabelsArray}
        style={{ minWidth: '650px' }}>
        <Column
          field='Peripheral'
          header='Peripheral'
          body={PeripheralBodyTemplate}></Column>
        <Column
          field='Enable'
          header='Enable'
          body={EnableBodyTemplate}></Column>
        <Column
          field='Source'
          header='Source'
          body={SourceBodyTemplate}></Column>

        <Column
          field='Peripheral Clock Frequency'
          header='Peripheral Clock Frequency'
          body={FrequencyBodyTemplate}></Column>
      </DataTable>
    </div>
  );
};
export default GenericClockConfiguration;
