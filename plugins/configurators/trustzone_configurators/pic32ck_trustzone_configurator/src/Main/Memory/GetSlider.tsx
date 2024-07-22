import { Slider } from 'primereact/slider';
import { GetBoxBottomHeight, GetBoxTopHeight, sliderPaddingRight, sliderWidth } from './Memory';

const GetSlider = (props: {
  sliderTopText: string;
  sliderBottomText: string;
  sliderValue: any;
  sliderMin: any;
  sliderMax: any;
  sliderHeight: any;
  updateSliderValue: (arg0: any) => void;
}) => {
  let topTextHeight = GetBoxTopHeight(props.sliderValue, props.sliderMax, props.sliderHeight);
  let bottomTextHeight = GetBoxBottomHeight(props.sliderValue, props.sliderMax, props.sliderHeight);
  let bTopTextVisibleStatus = props.sliderValue !== props.sliderMax;
  let bBottomTextVisibleStatus = props.sliderValue !== props.sliderMin;
  return (
    <div className='flex flex-row'>
      <div>
        <div className='flex flex-column flex justify-content-center flex-wrap card-container'>
          <div
            className='flex align-items-center justify-content-center'
            style={{
              width: sliderPaddingRight,
              height: topTextHeight + 'rem'
            }}>
            <div style={{ transform: 'rotate(-90deg)' }}>
              {bTopTextVisibleStatus && props.sliderTopText}
            </div>
          </div>
          <div
            className='flex align-items-center justify-content-center'
            style={{
              width: sliderPaddingRight,
              height: bottomTextHeight + 'rem'
            }}>
            <div style={{ transform: 'rotate(-90deg)' }}>
              {bBottomTextVisibleStatus && props.sliderBottomText}
            </div>
          </div>
        </div>
      </div>
      <div>
        <Slider
          value={props.sliderValue}
          min={props.sliderMin}
          max={props.sliderMax}
          style={{ height: props.sliderHeight + 'rem', width: sliderWidth + 'px' }}
          onChange={(e: any) => props.updateSliderValue(e.value)}
          orientation='vertical'
        />
      </div>
    </div>
  );
};

export default GetSlider;
