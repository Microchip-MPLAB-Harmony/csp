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
import { component_id } from '../MainView/MainBlock';
import { DataTable } from 'primereact/datatable';
import { Column } from 'primereact/column';
import { GetSymbolArray } from '@mplab_harmony/harmony-plugin-core-service/build/database-access/SymbolAccess';
import { GetUIComponentWithOutLabel } from '@mplab_harmony/harmony-plugin-ui/build/components/Components';
import { AddSymboLabelWithSuffix } from 'clock-common/lib/ClockUtils/ClockLabelUtils';

const GenericClockConfiguration = () => {
  let channelPeripipheralMap = GetSymbolArray(
    component_id,
    'GCLK_INSTANCE_PID'
  );
  let customLabelsArray = createCustomLengthArray();

  function createCustomLengthArray() {
    let dataArr = [];
    for (let i = 0; i < channelPeripipheralMap.length; i++) {
      dataArr.push({ id: i });
    }
    return dataArr;
  }

  const PeripheralBodyTemplate = (rowData: any) => {
    return <div>{channelPeripipheralMap[rowData.id]}</div>;
  };

  function ValueChange(onChangeData: Map<String, any>) {
    // do nothing
  }

  const EnableBodyTemplate = (rowData: any) => {
    return (
      <div>
        <GetUIComponentWithOutLabel
          componentId={component_id}
          symbolId={'CLK_' + channelPeripipheralMap[rowData.id] + '_GCLKEN'}
          onChange={ValueChange}
          symbolListeners={[
            'CLK_' + channelPeripipheralMap[rowData.id] + '_GCLKEN',
          ]}
        />
      </div>
    );
  };

  const SourceBodyTemplate = (rowData: any) => {
    return (
      <div>
        <GetUIComponentWithOutLabel
          componentId={component_id}
          symbolId={'CLK_' + channelPeripipheralMap[rowData.id] + '_GCLKCSS'}
          onChange={ValueChange}
          symbolListeners={[
            'CLK_' + channelPeripipheralMap[rowData.id] + '_GCLKCSS',
          ]}
        />
      </div>
    );
  };

  const DivisorBodyTemplate = (rowData: any) => {
    return (
      <div>
        <GetUIComponentWithOutLabel
          componentId={component_id}
          symbolId={'CLK_' + channelPeripipheralMap[rowData.id] + '_GCLKDIV'}
          onChange={ValueChange}
          symbolListeners={[
            'CLK_' + channelPeripipheralMap[rowData.id] + '_GCLKDIV',
          ]}
        />
      </div>
    );
  };

  const FrequencyBodyTemplate = (rowData: any) => {
    return (
      <div>
        {AddSymboLabelWithSuffix(
          channelPeripipheralMap[rowData.id] + '_GCLK_FREQUENCY',
          component_id,
          channelPeripipheralMap[rowData.id] + '_GCLK_FREQUENCY',
          ' Hz'
        )}
      </div>
    );
  };

  return (
    <div>
      <div className="p-d-flex">
        <div className="card">
          <DataTable
            value={customLabelsArray}
            stripedRows
            showGridlines
            responsiveLayout="scroll"
            style={{ width: '650px' }}
          >
            <Column
              field="Peripheral"
              header="Peripheral"
              body={PeripheralBodyTemplate}
            ></Column>
            <Column
              field="Enable"
              header="Enable"
              body={EnableBodyTemplate}
            ></Column>
            <Column
              field="Source"
              header="Source"
              body={SourceBodyTemplate}
            ></Column>
            <Column
              field="Divisor"
              header="Divisor"
              body={DivisorBodyTemplate}
            ></Column>
            <Column
              field="Frequency"
              header="Frequency"
              body={FrequencyBodyTemplate}
            ></Column>
          </DataTable>
        </div>
      </div>
    </div>
  );
};
export default GenericClockConfiguration;
