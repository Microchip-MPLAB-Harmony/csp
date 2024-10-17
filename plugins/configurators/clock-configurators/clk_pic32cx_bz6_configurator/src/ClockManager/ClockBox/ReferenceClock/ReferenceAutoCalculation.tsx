import PlainLabel from 'clock-common/lib/Components/LabelComponent/PlainLabel';
import { Button } from 'primereact/button';
import { InputNumber } from 'primereact/inputnumber';
import { GetClockDisplayFreqValue } from 'clock-common/lib/Tools/Tools';
import { useState } from 'react';
import CustomLogic, { refInputFreqs } from '../CustomLogic/CustomLogic';
import { useIntegerSymbol } from '@mplab_harmony/harmony-plugin-client-lib';
import { cx } from '../../MainBlock';
const ReferenceAutoCalculation = (props: {
  index: number;
  componentId: string;
  intialTargetFrequency: number;
  close: () => void;
}) => {
  const refDiv = useIntegerSymbol({
    componentId: props.componentId,
    symbolId: 'CONFIG_SYS_CLK_RODIV' + props.index
  });
  const refTrim = useIntegerSymbol({
    componentId: props.componentId,
    symbolId: 'CONFIG_SYS_CLK_ROTRIM' + props.index
  });

  const [spnTargetFrequency, setSpnTargetFrequency] = useState(props.intialTargetFrequency);
  const [bestOutputFreq, setBestOutputFreq] = useState(props.intialTargetFrequency);
  const [error, SetError] = useState(0);
  const [buttonDisable, setButtonDisable] = useState(true);
  const [inputFreq, setInputFreq] = useState(refInputFreqs[props.index - 1]);

  let _closestFrequency = props.intialTargetFrequency;
  let _rodivEstimate = refDiv.value;
  let _rotrimEstimate = refTrim.value;

  const calcualteFrequency = () => {
    let refclkOutputDivider = 0;
    let refclkTrimValue = 0;
    let tempNumber = 0;
    let integerPart = 0;
    let floatPart = 0;
    let tempFrequency = 0;
    let closestFrequency = 0;
    let targetFrequency = spnTargetFrequency;

    tempNumber = inputFreq / (targetFrequency * 2);
    integerPart = tempNumber;
    refclkOutputDivider = integerPart;
    floatPart = tempNumber - integerPart;

    if (refclkOutputDivider > 0 && refclkOutputDivider <= 65535) {
      tempNumber = floatPart * 512;
      refclkTrimValue = tempNumber;

      if (refclkTrimValue > 511) {
        refclkTrimValue = 511;
      } else if (refclkTrimValue < 0) {
        refclkTrimValue = 0;
      }

      _rodivEstimate = refclkOutputDivider;
      _rotrimEstimate = refclkTrimValue;

      closestFrequency = inputFreq / (2.0 * (refclkOutputDivider + refclkTrimValue / 512));

      _closestFrequency = closestFrequency;

      setButtonDisable(false);
    } else if (refclkOutputDivider === 0) {
      _rodivEstimate = refclkOutputDivider;
      _rotrimEstimate = 0;
      let half = inputFreq / 2;
      let temp = half + half / 2;
      if (targetFrequency > half && targetFrequency <= temp) {
        closestFrequency = half;
        _rodivEstimate = 1;
      } else {
        closestFrequency = inputFreq;
      }
      _closestFrequency = closestFrequency;

      setButtonDisable(false);
    } else {
      refclkOutputDivider = 0;
      refclkTrimValue = 0;

      if (_closestFrequency !== targetFrequency) {
        // lbl_bestOutputFreq.setForeground(Color.red);
        // lbl_percentError.setForeground(Color.red);
      } else {
        closestFrequency = targetFrequency;
      }

      setButtonDisable(false);
    }

    let percentError = (Math.abs(closestFrequency - targetFrequency) / targetFrequency) * 100;

    setBestOutputFreq(closestFrequency);
    SetError(percentError);
  };
  const accept = () => {};
  const cancel = () => {
    props.close();
  };
  const targetFreqChanged = (newValue: any) => {
    setSpnTargetFrequency(newValue);
    calcualteFrequency();
    setButtonDisable(false);
  };
  return (
    <div>
      <div className='grid'>
        <div className='col-6'>
          <PlainLabel
            disPlayText={'Target Reference Frequency'}
            className={''}
          />
        </div>
        <div className='col-6'>
          <div className='flex flex-row'>
            <InputNumber
              value={spnTargetFrequency}
              showButtons
              onValueChange={(target) => targetFreqChanged(target.value)}
            />
            <PlainLabel
              disPlayText={' Hz'}
              className={'m-2'}
            />
          </div>
        </div>
      </div>
      <div className='grid'>
        <div className='col-6'>
          <PlainLabel
            disPlayText={'REFCLK Input Frequency'}
            className={''}
          />
        </div>

        <div className='col-6'>
          <PlainLabel
            disPlayText={GetClockDisplayFreqValue(inputFreq)}
            className={''}
          />
        </div>
      </div>
      <div className='grid'>
        <div className='col-6'>
          <PlainLabel
            disPlayText={'Best Achievable Frequency'}
            className={''}
          />
        </div>

        <div className='col-6'>
          <PlainLabel
            disPlayText={GetClockDisplayFreqValue(bestOutputFreq)}
            className={''}
          />
        </div>
      </div>
      <div className='grid'>
        <div className='col-6'>
          <PlainLabel
            disPlayText={'% Error'}
            className={''}
          />
        </div>
        <div className='col-6'>
          <PlainLabel
            disPlayText={error + ' %'}
            className={''}
          />
        </div>
      </div>
      <div className=''>
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
              disabled={buttonDisable}
            />
          </div>
        </div>
      </div>
      {/* <CustomLogic cx={cx} /> */}
    </div>
  );
};
export default ReferenceAutoCalculation;
