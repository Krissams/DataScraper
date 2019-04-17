<?php

namespace App\Http\Controllers;
use Goutte\Client;
use GuzzleHttp\Client as GuzzleClient;
use Symfony\Component\DomCrawler\Crawler;


class ScrapeController extends Controller
{
    /**
     * Create a new controller instance.
     *
     * @return void
     */
    private $payload = [];
    private $totalPage = 0;


    public function __construct()
    {
    }

    public function index(){
       $this->client('https://www.yelp.com/search?find_desc=Restaurants&find_loc=San+Francisco%2C+CA&ns=1',1);
    }

    protected function client($url, $type = 1){
        if($type=1){
            $output = $this->getSite($url);
            $itemPerPage = 30;
            //Detect Total Num Page
            $output['result']->filter('.border-color--default__373c0__2oFDT .text-align--center__373c0__1l506 > span')->each(function ($node ) {
                $this->totalPage = str_replace('Page 1 of ','',$node->text());
            });
            $this->totalPage = 1; // TEST
            for ($i=1; $i <= $this->totalPage ; $i++) { 
                $start = $itemPerPage * $i; 
                $url . '&start=' . $start;
                $output = $this->getSite($url);

                //Load Information
                $output['result']->filter('h3 > a')->each(function ($node ) {
                    if( substr( $node->attr('href'), 0, 5 ) === '/biz/' ) {
                        $data = [
                            'name'=> $node->text(),
                            'uri'=>'https://www.yelp.com/' . $node->attr('href')
                        ];

                        $clientInfo = $this->getSite('https://www.yelp.com/' . $node->attr('href'));
                        
                        //Get Phone
                        $data['phone'] = $clientInfo['result']->filter('.biz-phone')->each(function ($nodes) {
                            $result = preg_replace('/[^A-Za-z0-9\-]/', '', $nodes->text());
                            return $result; 
                        });

                        
                        array_push($this->payload,$data);
                        dd($this->payload);
                        
                        
                    }
                    
                });
            }

            dd($this->payload);
        }
    }


    protected function getSite($url){
        $parse_url = parse_url($url);
        $client = new Client();
        $output = [
            'host' => $parse_url['host'],
            'result' => $client->request('GET',  $url)
        ];
        return $output;
    }
}
