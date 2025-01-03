import PlainLabel from 'clock-common/lib/Components/LabelComponent/PlainLabel';
import { Button } from 'primereact/button';
import { InputNumber } from 'primereact/inputnumber';
import { useState } from 'react';
import { configSymbolApi, useIntegerSymbol } from '@mplab_harmony/harmony-plugin-client-lib';
import { Dropdown } from 'primereact/dropdown';
import { Divider } from 'primereact/divider';
import {
  INPUT_MAX_FREQUENCY,
  INPUT_MIN_FREQUENCY,
  OUTPUT_MAX_FREQUENCY,
  OUTPUT_MIN_FREQUENCY
} from './FDPLLController';

const FDPLLAutoCalculation = (props: {
  componentId: string;
  expectedOutputFreq: number;
  clockSourceItems: string[];
  selectedClockIndex: number;
  ldrInt: number;
  ldrFrac: number;
  dpllDiv: number;
  close: () => void;
}) => {
  const XOSC32K_FREQ = useIntegerSymbol({
    componentId: props.componentId,
    symbolId: 'XOSC32K_FREQ'
  });
  const XOSC_FREQ = useIntegerSymbol({
    componentId: props.componentId,
    symbolId: 'XOSC_FREQ'
  });
  const GCLK_ID_0_FREQ = useIntegerSymbol({
    componentId: props.componentId,
    symbolId: 'GCLK_ID_0_FREQ'
  });

  const CONFIG_CLOCK_DPLL_LDR_INTEGER = useIntegerSymbol({
    componentId: props.componentId,
    symbolId: 'CONFIG_CLOCK_DPLL_LDR_INTEGER'
  });

  const CONFIG_CLOCK_DPLL_DIVIDER = useIntegerSymbol({
    componentId: props.componentId,
    symbolId: 'CONFIG_CLOCK_DPLL_DIVIDER'
  });

  const [expectedOutput, setExpectedOutput] = useState<number>(props.expectedOutputFreq);
  const [clockSourceInput, setClockSourceInput] = useState<String>(
    props.clockSourceItems[props.selectedClockIndex]
  );
  const [ldrInt, setLdrInt] = useState<number>(props.ldrInt);
  const [ldrFraction, setLdrFraction] = useState<number>(props.ldrFrac);
  const [fdpllOutputFreq, setFdpllOutputFreq] = useState<number>(expectedOutput);
  const [error, setError] = useState<number>(0.0);

  const accept = () => {
    configSymbolApi.setValue(props.componentId, 'CONFIG_CLOCK_DPLL_LDR_INTEGER', ldrInt);
    configSymbolApi.setValue(props.componentId, 'CONFIG_CLOCK_DPLL_LDRFRAC_FRACTION', ldrFraction);
    configSymbolApi.setValue(props.componentId, 'CONFIG_CLOCK_DPLL_REF_CLOCK', clockSourceInput);
    props.close();
  };
  const cancel = () => {
    props.close();
  };
  const targetFreqChanged = (newValue: any) => {
    setExpectedOutput(newValue);
    newCalculate(newValue);
    // setButtonDisable(false);
  };

  const clockSourceChanged = (newValue: any) => {
    setClockSourceInput(newValue);
    newCalculate(expectedOutput);
    // setButtonDisable(false);
  };

  const getInputFrequency = () => {
    let freq = 0;
    if (clockSourceInput.startsWith('XOSC32K')) {
      return XOSC32K_FREQ.value;
    } else if (clockSourceInput.startsWith('XOSC')) {
      freq = XOSC_FREQ.value / (2 * (props.dpllDiv + 1));
      return freq;
    } else if (clockSourceInput.startsWith('GCLK_DPLL')) {
      return GCLK_ID_0_FREQ.value;
    }
    return 0;
  };
  const invalidInput = () => {
    let i = getInputFrequency();
    return i < INPUT_MIN_FREQUENCY || i > INPUT_MAX_FREQUENCY;
  };
  const invalidOutput = () => {
    let i = expectedOutput;
    return i < OUTPUT_MIN_FREQUENCY || i > OUTPUT_MAX_FREQUENCY;
  };

  const newCalculate = (expectedOutput: number) => {
    let div = props.dpllDiv;
    let p1: Possibility | null = {
      ldrInt: props.ldrInt,
      ldrFraction: props.ldrFrac,
      fdpllOutputFreq: expectedOutput,
      error: 0
    };

    let delta1 = 2147483647;
    let delta2 = 2147483647;
    let delta3 = 2147483647;

    let opFreq = expectedOutput;
    let ipFreq = getInputFrequency();

    let m1 = Math.round(((opFreq * 1) / ipFreq) * 1000) / 1000;

    if (m1 < 1) {
      // avoid m1 combination; because expected output freqency is less than achievable range
      p1 = null;
    } else {
      let i1 = Math.floor(m1 - 1);
      let f1 = Math.floor(Math.round((m1 - i1 - 1) * 16));

      if (i1 > CONFIG_CLOCK_DPLL_LDR_INTEGER.min && i1 < CONFIG_CLOCK_DPLL_LDR_INTEGER.max) {
        p1.ldrInt = i1;
        p1.ldrFraction = f1;
        div = 1;
        p1.fdpllOutputFreq = calculateOutputFreqency(ipFreq, p1.ldrInt, p1.ldrFraction, 0);
        p1.error = Number(((Math.abs(opFreq - p1.fdpllOutputFreq) * 100) / opFreq).toFixed(3));
        delta1 = Math.abs(opFreq - p1.fdpllOutputFreq);
        if (p1.fdpllOutputFreq < OUTPUT_MIN_FREQUENCY) {
          let tempF1 = f1 + 1;
          p1 = fnreturnObtainedOutputFrequency(i1, tempF1, p1, ipFreq, opFreq);
        }
      } else {
        p1 = null;
      }
    }
    if (p1 !== null && (p1.fdpllOutputFreq === opFreq || (delta1 <= delta2 && delta1 <= delta3))) {
      setLdrInt(p1.ldrInt);
      setLdrFraction(p1.ldrFraction);
      setFdpllOutputFreq(p1.fdpllOutputFreq);
      setError(p1.error);
      return;
    }
  };
  function calculateOutputFreqency(
    inputFrequency: number,
    ldrInt: number,
    ldrFraction: number,
    outputPrescale: number
  ): number {
    return (
      inputFrequency * (ldrInt + 1.0 + ldrFraction / 16.0) * (1.0 / Math.pow(2, outputPrescale))
    );
  }
  interface Possibility {
    ldrInt: number;
    ldrFraction: number;
    fdpllOutputFreq: number;
    error: number;
  }

  const fnreturnObtainedOutputFrequency = (
    i1: number,
    f1: number,
    p1: Possibility | null,
    ipFreq: number,
    opFreq: number
  ): Possibility | null => {
    if (!p1) return null;
    if (i1 > CONFIG_CLOCK_DPLL_LDR_INTEGER.min && i1 < CONFIG_CLOCK_DPLL_LDR_INTEGER.max) {
      p1.ldrInt = i1;
      p1.ldrFraction = f1;
      p1.fdpllOutputFreq = calculateOutputFreqency(ipFreq, p1.ldrInt, p1.ldrFraction, 0);
      p1.error = (Math.abs(opFreq - p1.fdpllOutputFreq) * 100) / opFreq;
      if (p1.fdpllOutputFreq < OUTPUT_MIN_FREQUENCY) {
        let f2 = f1 + 1;
        p1 = fnreturnObtainedOutputFrequency(i1, f2, p1, ipFreq, opFreq);
      }
      return p1;
    }
    return null;
  };

  return (
    <div>
      <div className='grid'>
        <div className='col-6 text-right'>
          <div className='flex flex-column'>
            <PlainLabel disPlayText={'Desired DCO Output Frequency : '} />
            <PlainLabel disPlayText={'(48 MHz to  96 MHz)'} />
          </div>
        </div>
        <div className='col-6'>
          <div className='flex flex-column'>
            <div className='flex flex-row'>
              <InputNumber
                value={expectedOutput}
                showButtons
                onValueChange={(target) => targetFreqChanged(target.value)}
              />
              <PlainLabel
                disPlayText={' Hz'}
                className={'m-2'}
              />
            </div>
            {invalidOutput() && (
              <PlainLabel
                disPlayText={'Invalid Output Frequency Range ! ! !'}
                redColorStatus={true}
              />
            )}
          </div>
        </div>
      </div>
      <div className='grid'>
        <div className='col-6  text-right'>
          <div className='flex flex-column'>
            <PlainLabel disPlayText={'Select Reference Clock Source :'} />
            <PlainLabel disPlayText={'(32 KHz to  2 MHz)'} />
          </div>
        </div>

        <div className='col-6'>
          <div className='flex flex-column'>
            <Dropdown
              value={clockSourceInput}
              options={props.clockSourceItems}
              onChange={(e) => clockSourceChanged(e.value)}
            />
            {invalidInput() && (
              <PlainLabel
                disPlayText={'Invalid Input Frequency Range ! ! !'}
                redColorStatus={true}
              />
            )}
          </div>
        </div>
      </div>
      <Divider />
      <div className='grid'>
        <div className='col-6 text-right'>
          <PlainLabel disPlayText={'LDR Integer part :'} />
        </div>
        <div className='col-6  text-right'>
          <PlainLabel disPlayText={ldrInt + ''} />
        </div>
      </div>
      <div className='grid'>
        <div className='col-6  text-right'>
          <PlainLabel disPlayText={'LDR Fractional part :'} />
        </div>
        <div className='col-6  text-right'>
          <PlainLabel disPlayText={ldrFraction + ''} />
        </div>
      </div>
      <div className='grid'>
        <div className='col-6  text-right'>
          <PlainLabel disPlayText={'XOSC Input Divider value :'} />
        </div>
        <div className='col-6  text-right'>
          <PlainLabel disPlayText={props.dpllDiv + ''} />
        </div>
      </div>
      <div className='grid'>
        <div className='col-6  text-right'>
          <PlainLabel disPlayText={'Achievable DCO Output Freqency :'} />
        </div>
        <div className='col-6  text-right'>
          <PlainLabel disPlayText={fdpllOutputFreq + ''} />
        </div>
      </div>
      <div className='grid'>
        <div className='col-6  text-right'>
          <PlainLabel disPlayText={'% Error :'} />
        </div>
        <div className='col-6  text-right'>
          <PlainLabel disPlayText={error + ' %'} />
        </div>
      </div>
      <div className='flex flex-row-reverse'>
        <div className='flex align-items-center justify-content-center m-2'>
          <Button
            label={'Cancel'}
            onClick={cancel}
          />
        </div>
        <div className='flex align-items-center justify-content-center m-2'>
          <Button
            label={'Accept'}
            onClick={accept}
            // disabled={buttonDisable}
          />
        </div>
      </div>
    </div>
  );
};
export default FDPLLAutoCalculation;
