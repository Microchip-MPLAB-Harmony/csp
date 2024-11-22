import PlainLabel from 'clock-common/lib/Components/LabelComponent/PlainLabel';
import { Button } from 'primereact/button';
import { InputNumber } from 'primereact/inputnumber';
import { useState } from 'react';
import { Divider } from 'primereact/divider';
import { GetClockDisplayFreqValue } from 'clock-common/lib/Tools/Tools';
import { configSymbolApi } from '@mplab_harmony/harmony-plugin-client-lib';

let _pllidivEstimate = 0;
let _pllodivEstimate1 = 0;
let _pllodivEstimate2 = 0;
let _pllfbEstimate = 0;

const EthernetAutoCalculation = (props: {
  componentId: string;
  ethclk1: number;
  ethclk2: number;
  ethclkPllInputFreq: number;
  close: () => void;
}) => {
  const [ethClk1, setEthClk1] = useState<number>(props.ethclk1);
  const [ethClk2, setEthClk2] = useState<number>(props.ethclk1);
  const [bestAchievableEth1, setBestAchievableEth1] = useState<number>(props.ethclk1);
  const [bestAchievableEth2, setBestAchievableEth2] = useState<number>(props.ethclk2);
  const [errorEth1, setErrorEth1] = useState<number>(0.0);
  const [errorEth2, setErrorEth2] = useState<number>(0.0);
  const [buttonDisable, setButtonDisable] = useState(true);

  const singleDecimalFormat = new Intl.NumberFormat('en-US', {
    minimumFractionDigits: 0,
    maximumFractionDigits: 5
  });

  const accept = () => {
    configSymbolApi.setValue(props.componentId, 'EPLLCON_EPLLFBDIV_VALUE', _pllfbEstimate);
    configSymbolApi.setValue(props.componentId, 'EPLLCON_EPLLPOSTDIV1_VALUE', _pllodivEstimate1);
    configSymbolApi.setValue(props.componentId, 'EPLLPOSTDIV2', _pllodivEstimate2);
    configSymbolApi.setValue(props.componentId, 'EPLLCON_EPLLREFDIV_VALUE', _pllidivEstimate);
    props.close();
  };
  const cancel = () => {
    props.close();
  };
  const ethclk1Changed = (newValue: any) => {
    setEthClk1(newValue);
    RecalculateFreqencies1();
    setButtonDisable(false);
  };
  const ethclk2Changed = (newValue: any) => {
    setEthClk2(newValue);
    RecalculateFreqencies2();
    setButtonDisable(false);
  };

  const RecalculateFreqencies1 = () => {
    let inputDivider = 0;
    let outputDivider = 0;
    let fbDivider = 0;
    let tempFrequency1: number = 0.0;
    let closestFrequency1: number = 0.0;
    let targetFrequencyLong1 = Math.floor(ethClk1);
    const targetFrequency1: number = targetFrequencyLong1;

    if (targetFrequencyLong1 === 50000000) {
      tempFrequency1 = ((props.ethclkPllInputFreq / 20) * 800) / 32;
      closestFrequency1 = tempFrequency1;
      _pllidivEstimate = 20;
      _pllodivEstimate1 = 32;
      _pllodivEstimate2 = 10;
      _pllfbEstimate = 800;
    } else if (targetFrequencyLong1 === 25000000) {
      tempFrequency1 = ((props.ethclkPllInputFreq / 1) * 20) / 32;
      closestFrequency1 = tempFrequency1;
      _pllidivEstimate = 1;
      _pllodivEstimate1 = 32;
      _pllodivEstimate2 = 5;
      _pllfbEstimate = 20;
    } else {
      for (let iDiv = 1; iDiv <= 63; ++iDiv) {
        inputDivider = iDiv;

        for (let mult = 16; mult <= 1023; ++mult) {
          fbDivider = mult;

          for (let oDiv = 0; oDiv <= 63; ++oDiv) {
            if (oDiv === 0 || oDiv === 1) {
              outputDivider = 2;
            } else {
              outputDivider = 0x01 << oDiv;
            }

            tempFrequency1 =
              (props.ethclkPllInputFreq / inputDivider) * (fbDivider / outputDivider);

            const Fin: number = props.ethclkPllInputFreq / inputDivider;
            const Fvco: number = Fin * fbDivider;

            if (
              closestFrequency1 === 0 ||
              Math.abs(targetFrequency1 - tempFrequency1) <
                Math.abs(targetFrequency1 - closestFrequency1)
            ) {
              //Make sure Fin and Fvco are satisfied too
              if (
                Fin >= 5000000 &&
                Fin <= 64000000 &&
                Fvco >= 600000000 &&
                Fvco <= 1200000000 &&
                tempFrequency1 >= 10000000 &&
                tempFrequency1 <= 200000000
              ) {
                closestFrequency1 = tempFrequency1;
                _pllidivEstimate = inputDivider;
                _pllodivEstimate1 = outputDivider;
                _pllfbEstimate = fbDivider;
                _pllodivEstimate2 = _pllodivEstimate1 / 3;

                if (_pllodivEstimate2 < 1) {
                  _pllodivEstimate2 = 1;
                }
              }
            }
          }
        }
      }
    }
    const percentError: number =
      (Math.abs(closestFrequency1 - targetFrequency1) / targetFrequency1) * 100;

    setBestAchievableEth1(Math.floor(closestFrequency1));
    setErrorEth1(percentError);
  };

  const RecalculateFreqencies2 = () => {
    let inputDivider2 = 0;
    let outputDivider2 = 0;
    let fbDivider2 = 0;
    let tempFrequency2: number = 0.0;
    let closestFrequency2: number = 0.0;
    let targetFrequencyLong2 = Math.floor(ethClk2);
    const targetFrequency2: number = targetFrequencyLong2;
    if (targetFrequencyLong2 === 160000000) {
      tempFrequency2 = ((props.ethclkPllInputFreq / 20) * 800) / 10;
      closestFrequency2 = tempFrequency2;
      _pllidivEstimate = 20;
      _pllodivEstimate2 = 10;
      _pllodivEstimate1 = 32;
      _pllfbEstimate = 800;
    } else {
      for (let iDiv = 1; iDiv <= 63; ++iDiv) {
        inputDivider2 = iDiv;

        for (let mult = 16; mult <= 1023; ++mult) {
          fbDivider2 = mult;

          for (let oDiv = 0; oDiv <= 63; ++oDiv) {
            if (oDiv === 0 || oDiv === 1) {
              outputDivider2 = 2;
            } else {
              outputDivider2 = 0x01 << oDiv;
            }

            tempFrequency2 =
              ((props.ethclkPllInputFreq / inputDivider2) * fbDivider2) / outputDivider2;

            const Fin: number = props.ethclkPllInputFreq / inputDivider2;
            const Fvco: number = Fin * fbDivider2;

            if (
              closestFrequency2 === 0 ||
              Math.abs(targetFrequency2 - tempFrequency2) <
                Math.abs(targetFrequency2 - closestFrequency2)
            ) {
              //Make sure Fin and Fvco are satisfied too
              if (
                Fin >= 5000000 &&
                Fin <= 64000000 &&
                Fvco >= 600000000 &&
                Fvco <= 1200000000 &&
                tempFrequency2 >= 10000000 &&
                tempFrequency2 <= 200000000
              ) {
                closestFrequency2 = tempFrequency2;
                _pllidivEstimate = inputDivider2;
                _pllodivEstimate2 = outputDivider2;
                _pllfbEstimate = fbDivider2;
                _pllodivEstimate1 = _pllodivEstimate2 * 3;

                if (_pllodivEstimate2 > 63) {
                  _pllodivEstimate2 = 63;
                }
              }
            }
          }
        }
      }
    }
    const percentError2: number =
      (Math.abs(closestFrequency2 - targetFrequency2) / targetFrequency2) * 100;

    setBestAchievableEth2(Math.floor(closestFrequency2));
    setErrorEth2(percentError2);
  };

  return (
    <div>
      <div className='grid'>
        <div className='col-6 text-right'>
          <PlainLabel disPlayText={'Desired System Frequency for ETHCLK1 : '} />
        </div>
        <div className='col-6'>
          <div className='flex flex-row'>
            <InputNumber
              value={ethClk1}
              showButtons
              onValueChange={(target) => ethclk1Changed(target.value)}
            />
            <PlainLabel
              disPlayText={' Hz'}
              className={'m-2'}
            />
          </div>
        </div>
      </div>
      <div className='grid'>
        <div className='col-6  text-right'>
          <PlainLabel disPlayText={'PLL Input Frequency :'} />
        </div>
        <div className='col-6'>
          <PlainLabel disPlayText={GetClockDisplayFreqValue(props.ethclkPllInputFreq)} />
        </div>
      </div>
      <div className='grid'>
        <div className='col-6 text-right'>
          <PlainLabel disPlayText={'Best Achievable Frequency :'} />
        </div>
        <div className='col-6  '>
          <PlainLabel disPlayText={GetClockDisplayFreqValue(bestAchievableEth1)} />
        </div>
      </div>
      <div className='grid'>
        <div className='col-6  text-right'>
          <PlainLabel disPlayText={'% Error :'} />
        </div>
        <div className='col-6  '>
          <PlainLabel disPlayText={singleDecimalFormat.format(errorEth1) + ' %'} />
        </div>
      </div>
      <Divider />
      <div className='grid'>
        <div className='col-6 text-right'>
          <PlainLabel disPlayText={'Desired System Frequency for ETHCLK2 : '} />
        </div>
        <div className='col-6'>
          <div className='flex flex-row'>
            <InputNumber
              value={ethClk2}
              showButtons
              onValueChange={(target) => ethclk2Changed(target.value)}
            />
            <PlainLabel
              disPlayText={' Hz'}
              className={'m-2'}
            />
          </div>
        </div>
      </div>
      <div className='grid'>
        <div className='col-6  text-right'>
          <PlainLabel disPlayText={'PLL Input Frequency :'} />
        </div>
        <div className='col-6'>
          <PlainLabel disPlayText={GetClockDisplayFreqValue(props.ethclkPllInputFreq)} />
        </div>
      </div>
      <div className='grid'>
        <div className='col-6 text-right'>
          <PlainLabel disPlayText={'Best Achievable Frequency :'} />
        </div>
        <div className='col-6'>
          <PlainLabel disPlayText={GetClockDisplayFreqValue(bestAchievableEth2)} />
        </div>
      </div>
      <div className='grid'>
        <div className='col-6  text-right'>
          <PlainLabel disPlayText={'% Error :'} />
        </div>
        <div className='col-6'>
          <PlainLabel disPlayText={singleDecimalFormat.format(errorEth2) + ' %'} />
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
            disabled={buttonDisable}
          />
        </div>
      </div>
    </div>
  );
};
export default EthernetAutoCalculation;
