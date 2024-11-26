import PlainLabel from 'clock-common/lib/Components/LabelComponent/PlainLabel';
import { Button } from 'primereact/button';
import { InputNumber } from 'primereact/inputnumber';
import { useEffect, useState } from 'react';
import { Divider } from 'primereact/divider';
import { GetClockDisplayFreqValue } from 'clock-common/lib/Tools/Tools';
import {
  configSymbolApi,
  useCommentSymbol,
  useStringSymbol
} from '@mplab_harmony/harmony-plugin-client-lib';

const EthernetAutoCalculation = (props: {
  componentId: string;
  ethclk1: number;
  ethclk2: number;
  ethclkPllInputFreq: number;
  close: (acceptStatus: boolean) => void;
}) => {
  const [eth1Change, setEth1Change] = useState(false);
  const [eth2Change, seteth2Change] = useState(false);
  const [eth1ClockDisplayValue, setEth1ClockDisplayValue] = useState(props.ethclk1);
  const [eth2ClockDisplayValue, setEth2ClockDisplayValue] = useState(props.ethclk2);
  const symbol_ETHCLK1_freq = useStringSymbol({
    componentId: props.componentId,
    symbolId: 'ETHCLK1'
  });
  const symbol_ETHCLK2_freq = useStringSymbol({
    componentId: props.componentId,
    symbolId: 'ETHCLK2'
  });
  const symbol_ETHCLK1_error = useStringSymbol({
    componentId: props.componentId,
    symbolId: 'EPLL1_ERROR_PERC'
  });
  const symbol_ETHCLK2_error = useStringSymbol({
    componentId: props.componentId,
    symbolId: 'EPLL2_ERROR_PERC'
  });
  const epllOutOfRange = useCommentSymbol({
    componentId: props.componentId,
    symbolId: 'EPLL_AUTO_CALC_ERROR_MSG'
  });
  useEffect(() => {
    setButtonDisable(epllOutOfRange.visible);
  }, [epllOutOfRange]);

  const [buttonDisable, setButtonDisable] = useState(true);

  const singleDecimalFormat = new Intl.NumberFormat('en-US', {
    minimumFractionDigits: 0,
    maximumFractionDigits: 5
  });

  const accept = () => {
    props.close(true);
  };
  const cancel = () => {
    props.close(false);
  };
  const ethclk1Changed = (newValue: number) => {
    RecalculateFreqencies1(newValue);
    setEth1ClockDisplayValue(newValue);
    setEth1Change(true);
    setButtonDisable(false);
  };
  const ethclk2Changed = (newValue: number) => {
    RecalculateFreqencies2(newValue);
    setEth2ClockDisplayValue(newValue);
    seteth2Change(true);
    setButtonDisable(false);
  };

  const RecalculateFreqencies1 = (newValue: number) => {
    configSymbolApi.setValue(props.componentId, 'EPLL1_REQUESTED_FOUT', newValue);
  };

  const RecalculateFreqencies2 = (newValue: number) => {
    configSymbolApi.setValue(props.componentId, 'EPLL2_REQUESTED_FOUT', newValue);
  };

  return (
    <div>
      <div className='grid'>
        <div className='col-6 text-right'>
          <PlainLabel disPlayText={'Desired Frequency for ETHCLK1 : '} />
        </div>
        <div className='col-6'>
          <div className='flex flex-column'>
            <div className='flex flex-row'>
              <InputNumber
                value={eth1ClockDisplayValue}
                showButtons
                onValueChange={(target) => ethclk1Changed(Number(target.value))}
              />
              <PlainLabel
                disPlayText={' Hz'}
                className={'m-2'}
              />
            </div>
            {epllOutOfRange.visible && (eth1Change || eth2Change) && (
              <PlainLabel
                disPlayText={epllOutOfRange.label}
                redColorStatus={true}
              />
            )}
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
          <PlainLabel
            disPlayText={GetClockDisplayFreqValue(Math.floor(Number(symbol_ETHCLK1_freq.value)))}
          />
        </div>
      </div>
      <div className='grid'>
        <div className='col-6  text-right'>
          <PlainLabel disPlayText={'% Error :'} />
        </div>
        <div className='col-6  '>
          <PlainLabel
            disPlayText={
              eth1Change
                ? singleDecimalFormat.format(Number(symbol_ETHCLK1_error.value)) + ' %'
                : '0.00 %'
            }
          />
        </div>
      </div>
      <Divider />
      <div className='grid'>
        <div className='col-6 text-right'>
          <PlainLabel disPlayText={'Desired Frequency for ETHCLK2 : '} />
        </div>
        <div className='col-6'>
          <div className='flex flex-row'>
            <InputNumber
              value={eth2ClockDisplayValue}
              showButtons
              onValueChange={(target) => ethclk2Changed(Number(target.value))}
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
          <PlainLabel
            disPlayText={GetClockDisplayFreqValue(Math.floor(Number(symbol_ETHCLK2_freq.value)))}
          />
        </div>
      </div>
      <div className='grid'>
        <div className='col-6  text-right'>
          <PlainLabel disPlayText={'% Error :'} />
        </div>
        <div className='col-6'>
          <PlainLabel
            disPlayText={
              eth2Change
                ? singleDecimalFormat.format(Number(symbol_ETHCLK2_error.value)) + ' %'
                : '0.00 %'
            }
          />
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
