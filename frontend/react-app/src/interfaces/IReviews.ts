export default interface IReview {
  id?: number;
  user_id?: number;
  product_id?: number;
  rating?: number;
  comment?: string;
  created_at?: string;
}
