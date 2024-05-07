import { Tooltip } from "primereact/tooltip";
type Props =  {
    value:string
}
const CustomTooltip = ({value}:Props) => {
    return <Tooltip target={`.${value}`} mouseTrack={true} event="both" />;
  };

  export default CustomTooltip