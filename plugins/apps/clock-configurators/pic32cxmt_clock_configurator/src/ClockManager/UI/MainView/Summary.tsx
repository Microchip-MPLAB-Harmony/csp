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
import { Accordion, AccordionTab } from 'primereact/accordion';
import { Column } from 'primereact/column';
import { DataTable } from 'primereact/datatable';
import {
  component_id,
  GetCoreStatus,
  dualCoreString,
  singleCoreString,
} from './MainBlock';
import {
  GetSymbolArray,
  GetSymbolLabelName,
  GetSymbolValue,
} from '@mplab_harmony/harmony-plugin-core-service/build/database-access/SymbolAccess';

const SummaryPage = () => {
  function GetLabelAndValue(
    labelName: string,
    symbolId: string,
    appendString: string = ''
  ) {
    return (
      <div className="field grid">
        <div>
          <label style={{ fontSize: '14px' }} className="p-col">
            {' '}
            {'\u2022 ' + labelName + ' : '}
          </label>
        </div>
        <div className="p-col">
          <label style={{ fontSize: '14px' }} className="p-col">
            {GetSymbolValue(component_id, symbolId) + appendString}{' '}
          </label>
        </div>
      </div>
    );
  }

  function SlowClockSettings() {
    return (
      <div className="flex flex-column">
        {GetLabelAndValue('Source', 'CLK_TDXTALSEL')}
        {GetLabelAndValue('Bypass', 'CLK_OSCBYPASS')}
        {GetLabelAndValue('MD SLOW clock frequency', 'MD_SLOW_CLK_FREQUENCY')}
        {GetLabelAndValue('TD SLOW clock frequency', 'TD_SLOW_CLOCK_FREQUENCY')}
      </div>
    );
  }

  function MainClockSettings() {
    return (
      <div className="flex flex-column">
        {GetLabelAndValue(
          'Main RC Oscillator (12MHz) Osc Enable',
          'CLK_MOSCRCEN'
        )}
        {GetLabelAndValue('Startup Time', 'CLK_MOSCXTST')}
        {GetLabelAndValue(
          'Main Oscillator/External Clock Frequency',
          'CLK_MOSCXTFREQ',
          ' Hz'
        )}
        {GetLabelAndValue(
          'Main Crystal Oscillator (12 - 48MHz) Enable',
          'CLK_MOSCXTEN'
        )}
        {GetLabelAndValue('Main Clock Frequency', 'MAINCK_FREQUENCY', ' Hz')}
      </div>
    );
  }

  function PCKxClock(index: number) {
    return (
      <div className="flex flex-column">
        {GetLabelAndValue('PCLK CSS', 'CLK_PCK' + index + '_CSS')}
        {GetLabelAndValue('PCLK PRES', 'CLK_PCK' + index + '_PRES')}
        {GetLabelAndValue('PCLK Enable', 'CLK_SCER_PCK' + index)}
        {index === 0 &&
          GetLabelAndValue('PCLK0 Frequency', 'PCK0_FREQUENCY', ' Hz')}
        {index === 1 &&
          GetLabelAndValue('PCLK1 Frequency', 'PCK1_FREQUENCY', ' Hz')}
        {index === 2 &&
          GetLabelAndValue('PCLK2 Frequency', 'PCK2_FREQUENCY', ' Hz')}
      </div>
    );
  }

  function PLLChildrenControllerConfig(letter: any) {
    return (
      <div className="flex flex-column">
        {GetLabelAndValue('PLL Core Enable', 'CLK_PLL' + letter + '_ENPLL')}
        {GetLabelAndValue('Source', 'CLK_PLL' + letter + '_PLLMS')}
        {GetLabelAndValue('MUL', 'CLK_PLL' + letter + '_MUL')}
        {GetLabelAndValue('FRACR', 'CLK_PLL' + letter + '_FRACR')}
        {GetLabelAndValue(
          'Spread Spectrum Enable',
          'CLK_PLL' + letter + '_ENSPREAD'
        )}
        {GetLabelAndValue('STEP', 'CLK_PLL' + letter + '_STEP')}
        {GetLabelAndValue('NSTEP', 'CLK_PLL' + letter + '_NSTEP')}
        {GetLabelAndValue('ENPLLO0', 'CLK_PLL' + letter + '_ENPLLO0')}
        {GetLabelAndValue('DIVPMC0', 'CLK_PLL' + letter + '_DIVPMC0')}
        {letter === 'A' &&
          GetLabelAndValue('ENPLLO1', 'CLK_PLL' + letter + '_ENPLLO1')}
        {letter === 'A' &&
          GetLabelAndValue('DIVPMC1', 'CLK_PLL' + letter + '_DIVPMC1')}
        {GetLabelAndValue(
          'PLL' + letter + ' Ref clock Freqency',
          'PLL' + letter + '_REFCLK_FREQUENCY',
          ' Hz'
        )}
        {GetLabelAndValue(
          'PLL ' + letter + ' Core clock Freqency',
          'PLL' + letter + '_CORECLK_FREQUENCY',
          ' Hz'
        )}
        {letter === 'A' &&
          GetLabelAndValue('PLLACK0 Freqency', 'PLLACK0_FREQUENCY', ' Hz')}
        {letter === 'A' &&
          GetLabelAndValue('PLLACK1 Freqency', 'PLLACK1_FREQUENCY', ' Hz')}
        {letter === 'B' &&
          GetLabelAndValue('PLLBCK Freqency', 'PLLBCK_FREQUENCY', ' Hz')}
        {letter === 'C' &&
          GetLabelAndValue('PLLCCK Freqency', 'PLLCCK_FREQUENCY', ' Hz')}
      </div>
    );
  }

  function DualCore0Controller() {
    return (
      <div className="field">
        <div className="p-fluid">
          <div className="field">
            <br></br>
            <span style={{ fontWeight: 'bold', fontSize: '14px' }}>
              {' '}
              Processor Clock Core 0 Controller{' '}
            </span>
          </div>
          <div className="field">{Core0Controller()}</div>
        </div>
      </div>
    );
  }

  function DualCore1Controller() {
    return (
      <div className="field">
        <div className="p-fluid">
          <div className="field">
            <br></br>
            <span style={{ fontWeight: 'bold', fontSize: '14px' }}>
              {' '}
              Processor Clock Core 1 Controller{' '}
            </span>
          </div>
          <div className="field">{Core1Controller()}</div>
        </div>
      </div>
    );
  }

  function SingleCoreController() {
    return (
      <div>
        <div className="field">
          <div className="p-fluid">
            <div className="field">
              <br></br>
              <span style={{ fontWeight: 'bold', fontSize: '14px' }}>
                {' '}
                Processor Clock Single Core Controller{' '}
              </span>
            </div>
            <div className="field">{SingleCoreSettings()}</div>
          </div>
        </div>
      </div>
    );
  }

  function SingleCoreSettings() {
    return (
      <div className="flex flex-column">
        {Core0Controller()}
        {Core1Controller()}
      </div>
    );
  }

  function Core0Controller() {
    return (
      <div className="flex flex-column">
        {GetLabelAndValue('CSS', 'CLK_CPU_CKR_CSS')}
        {GetLabelAndValue('PRES', 'CLK_CPU_CKR_PRES')}
        {GetLabelAndValue('MCK0DIV Enable', 'CLK_CPU_CKR_RATIO_MCK0DIV')}
        {GetLabelAndValue('MCK0DIV2 Enable', 'CLK_CPU_CKR_RATIO_MCK0DIV2')}
        {GetLabelAndValue('CPU clock frequency', 'CPU_CLOCK_FREQUENCY', ' Hz')}
        {GetLabelAndValue('MCK0 frequency', 'MCK0_FREQUENCY', ' Hz')}
        {GetLabelAndValue(
          'MCK0DIV Clock Frequency',
          'MCK0DIV_FREQUENCY',
          ' Hz'
        )}
        {GetLabelAndValue(
          'MCK0DIV2 Clock Frequency',
          'MCK0DIV2_FREQUENCY',
          ' Hz'
        )}
      </div>
    );
  }

  function Core1Controller() {
    return (
      <div className="flex flex-column">
        {GetLabelAndValue('CSS', 'CLK_CPU_CKR_CPCSS')}
        {GetLabelAndValue('PRES', 'CLK_CPU_CKR_CPPRES')}
        {GetLabelAndValue('CPBMCK Enable', 'CLK_SCER_CPBMCK')}
        {GetCoreStatus() === dualCoreString &&
          GetLabelAndValue('CPCK Enable', 'CLK_SCER_CPCK')}
        {GetLabelAndValue('MCK1DIV Enable', 'CLK_CPU_CKR_RATIO_MCK1DIV')}
        {GetCoreStatus() === dualCoreString &&
          GetLabelAndValue(
            'CPU Clock 1 frequency',
            'CPU1_CLOCK_FREQUENCY',
            ' Hz'
          )}
        {GetLabelAndValue('MCK1 frequency', 'MCK1_FREQUENCY', ' Hz')}
        {GetLabelAndValue(
          'MCK1DIV Clock Frequency',
          'MCK1DIV_FREQUENCY',
          ' Hz'
        )}
      </div>
    );
  }

  function GetProgrammableClocksfiguration() {
    return (
      <div className="formgroup-inline">
        <div className="field">
          <div className="p-fluid">
            <div className="field">
              <br></br>
              <span style={{ fontWeight: 'bold', fontSize: '14px' }}>
                {' '}
                PCK0 Controller{' '}
              </span>
            </div>
            <div className="field">{PCKxClock(0)}</div>
          </div>
        </div>
        <div className="field">
          <div className="p-fluid">
            <div className="field">
              <br></br>
              <span style={{ fontWeight: 'bold', fontSize: '14px' }}>
                {' '}
                PCK1 Controller{' '}
              </span>
            </div>
            <div className="field">{PCKxClock(1)}</div>
          </div>
        </div>
        <div className="field">
          <div className="p-fluid">
            <div className="field">
              <br></br>
              <span style={{ fontWeight: 'bold', fontSize: '14px' }}>
                {' '}
                PCK2 Controller{' '}
              </span>
            </div>
            <div className="field">{PCKxClock(2)}</div>
          </div>
        </div>
      </div>
    );
  }

  function GetPLLControllConfiguration() {
    return (
      <div className="formgroup-inline">
        <div className="field">
          <div className="p-fluid">
            <div className="field">
              <br></br>
              <span style={{ fontWeight: 'bold', fontSize: '14px' }}>
                {' '}
                PLLA Controller{' '}
              </span>
            </div>
            <div className="field">{PLLChildrenControllerConfig('A')}</div>
          </div>
        </div>
        <div className="field">
          <div className="p-fluid">
            <div className="field">
              <br></br>
              <span style={{ fontWeight: 'bold', fontSize: '14px' }}>
                {' '}
                PLLB Controller{' '}
              </span>
            </div>
            <div className="field">{PLLChildrenControllerConfig('B')}</div>
          </div>
        </div>
        <div className="field">
          <div className="p-fluid">
            <div className="field">
              <br></br>
              <span style={{ fontWeight: 'bold', fontSize: '14px' }}>
                {' '}
                PLLC Controller{' '}
              </span>
            </div>
            <div className="field">{PLLChildrenControllerConfig('C')}</div>
          </div>
        </div>
      </div>
    );
  }

  function GetPeripheralClockConfig() {
    let channelPeripipheralMap = GetSymbolArray(
      component_id,
      'PERIPHERAL_CLOCK_CONFIG'
    );

    function getChannelPeripheralCols() {
      let colsJsx = [];
      let cols = channelPeripipheralMap.length / 10;
      if (channelPeripipheralMap % 10 < 0) {
        cols = cols + 1;
      }

      for (let i: number = 0; i < cols; i++) {
        let start: number = 10 * i;
        let end: number = start + 10;
        if (end >= channelPeripipheralMap.length) {
          end = channelPeripipheralMap.length - 1;
        }
        colsJsx.push(getColumn(start, end));
      }
      return colsJsx;
    }

    function getColumn(startIndex: number, endIndex: number) {
      return (
        <div className="field">
          <div className="p-fluid">
            {getSymbolWithLabels(startIndex, endIndex)}
          </div>
        </div>
      );
    }

    function getSymbolWithLabels(startIndex: number, endIndex: number) {
      const arrLabelName = [];
      for (let i: number = startIndex; i < endIndex; i++) {
        arrLabelName.push(
          <div>
            {GetLabelAndValue(
              GetSymbolLabelName(component_id, channelPeripipheralMap[i]) +
                ' Enabled: ',
              channelPeripipheralMap[i]
            )}
          </div>
        );
      }
      return arrLabelName;
    }

    return <div className="formgroup-inline">{getChannelPeripheralCols()}</div>;
  }

  function GetGenericClockConfig() {
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

    const EnableBodyTemplate = (rowData: any) => {
      return (
        <div>
          {GetSymbolValue(
            component_id,
            'CLK_' + channelPeripipheralMap[rowData.id] + '_GCLKEN'
          )}
        </div>
      );
    };

    const SourceBodyTemplate = (rowData: any) => {
      return (
        <div>
          {GetSymbolValue(
            component_id,
            'CLK_' + channelPeripipheralMap[rowData.id] + '_GCLKCSS'
          )}
        </div>
      );
    };

    const DivisorBodyTemplate = (rowData: any) => {
      return (
        <div>
          {GetSymbolValue(
            component_id,
            'CLK_' + channelPeripipheralMap[rowData.id] + '_GCLKDIV'
          )}
        </div>
      );
    };

    const FrequencyBodyTemplate = (rowData: any) => {
      return (
        <div>
          {GetSymbolValue(
            component_id,
            channelPeripipheralMap[rowData.id] + '_GCLK_FREQUENCY'
          ) + ' Hz'}
        </div>
      );
    };

    return (
      <div className="formgroup-inline">
        <div className="p-d-flex">
          <div className="card">
            <DataTable
              value={customLabelsArray}
              stripedRows
              showGridlines
              responsiveLayout="scroll"
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
  }

  function GetClockConfig() {
    return (
      <div className="formgroup-inline">
        <div className="field">
          <div className="p-fluid">
            <div className="field">
              <br></br>
              <span style={{ fontWeight: 'bold', fontSize: '14px' }}>
                {' '}
                Slow clock{' '}
              </span>
            </div>
            <div className="field">{SlowClockSettings()}</div>
          </div>
        </div>
        <div className="field">
          <div className="p-fluid">
            <div className="field">
              <br></br>
              <span style={{ fontWeight: 'bold', fontSize: '14px' }}>
                {' '}
                Main clock{' '}
              </span>
            </div>
            <div className="field">{MainClockSettings()}</div>
          </div>
        </div>
        {GetCoreStatus() === dualCoreString && DualCore0Controller()}
        {GetCoreStatus() === dualCoreString && DualCore1Controller()}
        {GetCoreStatus() === singleCoreString && SingleCoreController()}
      </div>
    );
  }

  return (
    <div>
      <Accordion activeIndex={0}>
        <AccordionTab header="Clock Configuration">
          <div className="flex flex-column">{GetClockConfig()}</div>
        </AccordionTab>
        <AccordionTab header="PLL Controll Configuration">
          <div className="flex flex-column">
            {GetPLLControllConfiguration()}
          </div>
        </AccordionTab>
        <AccordionTab header="Programmable clocks Configuration">
          <div className="flex flex-column">
            {GetProgrammableClocksfiguration()}
          </div>
        </AccordionTab>
        <AccordionTab header="Peripheral Clock Configuration">
          <div className="flex flex-column">{GetPeripheralClockConfig()}</div>
        </AccordionTab>
        <AccordionTab header="Generic Clock Configuration">
          <div className="flex flex-column">{GetGenericClockConfig()}</div>
        </AccordionTab>
      </Accordion>
    </div>
  );
};

export default SummaryPage;
