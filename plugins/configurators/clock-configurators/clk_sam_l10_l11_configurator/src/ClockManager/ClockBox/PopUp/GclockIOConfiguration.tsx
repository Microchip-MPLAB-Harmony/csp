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
  InputNumberDefault,
  PluginConfigContext,
  useBooleanSymbol,
  useIntegerSymbol
} from '@mplab_harmony/harmony-plugin-client-lib';
import FrequencyLabelComponent from 'clock-common/lib/Components/LabelComponent/FrequencyLabelComponent';
import { Button } from 'primereact/button';

const PeripheralsConfiguration = () => {
  const { componentId = 'core' } = useContext(PluginConfigContext);
  const NumberofGenerators = useIntegerSymbol({ componentId, symbolId: 'GCLK_NUM_PADS' });

  let customLabelsArray = createCustomLengthArray();

  function createCustomLengthArray() {
    let dataArr = [];
    for (let i = 0; i < NumberofGenerators.value; i++) {
      dataArr.push({ id: i });
    }
    return dataArr;
  }

  const GeneratorBodyTemplate = (rowData: any) => {
    return <div>{rowData.id}</div>;
  };

  const InOutBodyTemplate = (rowData: any) => {
    const gclkOutPutEnable = useBooleanSymbol({
      componentId,
      symbolId: 'GCLK_' + rowData.id + '_OUTPUTENABLE'
    });
    return (
      <div>
        <Button
          label={gclkOutPutEnable.value ? 'Out' : 'In'}
          style={{ width: '50px' }}
          onClick={(event: React.MouseEvent<HTMLButtonElement>) => {
            const buttonText = event.currentTarget.textContent || event.currentTarget.innerText;
            if (buttonText === 'Out') {
              gclkOutPutEnable.writeValue(false);
            } else {
              gclkOutPutEnable.writeValue(true);
            }
          }}
        />
      </div>
    );
  };

  const InFrequencyBodyTemplate = (rowData: any) => {
    return (
      <div>
        <InputNumberDefault
          componentId={componentId}
          symbolId={'GCLK_IN_' + rowData.id + '_FREQ'}
        />
      </div>
    );
  };

  const OutFrequencyBodyTemplate = (rowData: any) => {
    return (
      <div>
        <FrequencyLabelComponent
          componentId={componentId}
          symbolId={'GCLK_IO_' + rowData.id + '_FREQ'}
          className={''}
        />
      </div>
    );
  };

  return (
    <div>
      <DataTable
        value={customLabelsArray}
        tableStyle={{ minWidth: '400px' }}>
        <Column
        style={{textAlign:'center'}}
          field='Generator'
          header='Generator'
          body={GeneratorBodyTemplate}></Column>
        <Column
        style={{textAlign:'center'}}
          field='In/Out'
          header='In/Out'
          body={InOutBodyTemplate}>
            
          </Column>
        <Column
        style={{textAlign:'center'}}
          field='In Frequency (Hz)'
          header='In Frequency (Hz)'
          body={InFrequencyBodyTemplate}></Column>
        <Column
        style={{textAlign:'center'}}
          field='Out Frequency (Hz)'
          header='Out Frequency (Hz)'
          body={OutFrequencyBodyTemplate}></Column>
      </DataTable>
    </div>
  );
};
export default PeripheralsConfiguration;
